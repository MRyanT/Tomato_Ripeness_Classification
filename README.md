# Tomato Ripeness Classification
![Tomato-Garden](https://github.com/user-attachments/assets/fac1e605-8e4f-42cc-a39b-fc8a5c249035)

## Anggota Kelompok
* Mikhael Ryan Toar		(215150300111006)
* Ni Made Ayu Astina Sari	(215150301111035)
* Mohammad Faiz Musharrif	(215150300111038)
* Hilmisyah Nabil		(215150307111026)
* Mush’ab Safirurrasul S	(215150307111040)

## Domain Projek
### Permasalahan
* Penentuan waktu panen yang tidak akurat menyebabkan kehilangan hasil hingga 20%, menurunkan kualitas produk dan merugikan petani.
* Kehilangan hasil merugikan pendapatan petani, melemahkan ketahanan pangan, dan meningkatkan limbah organik yang mencemari lingkungan.
* Metode manual untuk menentukan kematangan buah memakan waktu, tidak konsisten, dan sulit diterapkan pada skala besar.

### Solusi yang Ditawarkan
* Sistem berbasis edge yang memungkinkan pemantauan kematangan tomat secara otomatis dan konsisten.
* Sistem yang memungkinkan deteksi kematangan tomat di lokasi akses internet terbatas, sehingga ideal untuk perkebunan terpencil.
* Deteksi yang akurat meminimalkan kerusakan produk, meningkatkan kualitas hasil panen, dan mengurangi tingkat kehilangan hasil panen secara nasional.

## Struktur Sistem
### Hardware & Software
* Edge Server : Laptop
* Edge Device : Webcam
* Display Result : GUI
### Dataset
 <div align="justify">Dataset yang digunakan merupakan kumpulan gambar tomat matang dan belum matang yang telah diberi _label/annotasi_ dengan menggunakan roboflow. Roboflow juga digunakan untuk agumentasi data serta menyusun data untuk _Train, Test, dan Validation_ serta mengekspor dataaset dalam bentuk YOLOv10. Dataset tersebut disimpan dalam zip file yang berisi file-file gambar dan yaml file, dimana .yaml file harus diedit agar lokasi _train,test, dan validation_ sesuai dengan lokasi directory gambar-gambar. </div>

(file .yaml yang harus di edit)
* train: ../train/images
* val: ../valid/images
* test: ../test/images

### Arsitektur Umum
![Screenshot 2024-11-13 162834](https://github.com/user-attachments/assets/5623e596-5954-4d13-afc4-718008a1ddbb)
### Flowchart YOLOv10
![Flowchart YOLOv10](https://github.com/user-attachments/assets/fac05567-1ebf-4ee1-a8a9-a52b71ba67d1)
### Flowchart GUI
![Flowhcart GUI](https://github.com/user-attachments/assets/c87f3d88-0a41-40e9-9deb-09d317df3075)

## Menjalankan Sistem/Demo
![Tampilan Utama](https://github.com/user-attachments/assets/40a0a9af-7e45-40a3-b6c7-ab65fa77b2e3)

Sistem ini dapat dioperasikan menggunakan GUI, dimana GUI dapat dijalankan dengan memasukan kode 'streamlit run GUI.py(sesuai dengan nama file)'. Ketika dijalankan, akan membuka window baru pada browser yang akan menampilkan tampilan utama GUI dan memberikan 2 tombol, Live Webcam Detection dan Upload Image File.


### Live Webcam Detection

https://github.com/user-attachments/assets/b697e18e-47f5-4dee-b645-8391a87677d4

### Upload Image file
![Upload Image](https://github.com/user-attachments/assets/1f07286c-c034-464b-91d9-d1a82e1e4ab9)

## Kesimpulan
 <div align="justify"> Proyek ini bertujuan untuk mengembangkan sistem berbasis edge yang mampu mendeteksi tingkat kematangan tomat secara otomatis dan akurat. Sistem ini dirancang untuk membantu petani meningkatkan efisiensi panen dan mendorong keberlanjutan dalam pertanian, terutama di sektor urban farming dan perkebunan terpencil. Sistem ini juga bertujuan untuk mengatasi tantangan penentuan waktu panen yang tidak akurat, yang sering kali menyebabkan kehilangan hasil, menurunkan kualitas produk, dan meningkatkan limbah organik.

Pada saat ini, sistem ini berada pada tahap awal dan belum mencapai prototyping. Oleh karena itu, pengembangannya dapat dilanjutkan dengan mengimplementasikan perangkat edge ke dalam sistem. Langkah ini akan memungkinkan sistem untuk mencapai fungsi optimal sesuai kondisi lapangan yang sebenarnya, memberikan solusi yang lebih relevan dan aplikatif bagi petani. </div>
