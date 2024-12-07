import streamlit as st
import matplotlib.pyplot as plt
import os
import cv2
from ultralytics import YOLO
import numpy as np
import math
import time

st.title("Tomato Ripeness Classification!")
st.subheader("Aplikasi ini dibuat agar dapat melihat apakah suatu tomat sudah matang atau belum.")

# atur path sesuai dengan path model hasil training YOLO
model_path = "D:/Kuliah/Semester 7/Edge Inteligence/Project Akhir/Models/best.pt"

if 'model' not in st.session_state:
    st.session_state.model = YOLO(model_path)
if 'webcam_active' not in st.session_state:
    st.session_state.webcam_active = False

def test_yolo_image(model_path, image, confidence_threshold=0.5):
    if image is None:
        st.error("No image provided for processing!")
        return

    model = YOLO(model_path)
    
    if isinstance(image, np.ndarray):
        pass
    else:
        file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    results = model(image)[0]
    
    annotated_image = image.copy()
    for result in results.boxes:
        x1, y1, x2, y2 = result.xyxy[0].cpu().numpy().astype(int)
        conf = result.conf.cpu().numpy()[0]
        cls = int(result.cls.cpu().numpy()[0])
        
        if conf > confidence_threshold:
            class_name = model.names[cls]
            cv2.rectangle(annotated_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(annotated_image, f"{class_name}: {conf:.2f}", 
                        (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
    return annotated_image

def run_webcam_feed():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    stframe = st.empty()
    
    while st.session_state.webcam_active:
        success, img = cap.read()
        if not success:
            st.warning("Failed to access webcam.")
            break
        
        results = st.session_state.model(img, stream=True)
        
        for r in results:
            boxes = r.boxes
            for box in boxes:

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
                
                confidence = math.ceil((box.conf[0] * 100)) / 100
                
                cls = int(box.cls[0])
                class_name = st.session_state.model.names[cls]
                
                label = f"{class_name} {confidence:.2f}"
                cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        stframe.image(img, channels="RGB", use_container_width=True)
        
        time.sleep(0.03)
        
        if not st.session_state.webcam_active:
            break
    
    cap.release()
    cv2.destroyAllWindows()

# webcam feed button
if st.button("Live Webcam Detection"):
    # webcam active state
    st.session_state.webcam_active = not st.session_state.webcam_active
    
    # If webcam active, run the feed
    if st.session_state.webcam_active:
        run_webcam_feed()

# File upload 
uploaded_image = st.file_uploader("Upload image file", type=["jpg", "jpeg", "png"])
if uploaded_image is not None:
    if st.button("Process Image"):
        st.write("Processing image...")
        processed_image = test_yolo_image(model_path, uploaded_image)
        st.image(processed_image, caption="Processed Image", use_container_width=True)
else:
    st.warning("No image file!")
