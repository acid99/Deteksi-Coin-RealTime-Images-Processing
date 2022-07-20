# Deteksi-Koin-RealTime-Images-Processing

## <p align="center">Hasil Transmisi Secara Langsung</p>
<p align="center"><img src= "https://github.com/acid99/Deteksi-Koin-RealTime-Images-Processing/blob/main/hasil.png?raw=true"></p>

## <p align="center">Batasan Program</p>
- Hanya Mendeteksi Jumlah Koin 
- Background Pada Gambar Tidak Dapat Sewarna Dengan Warna Objek 
- Objek Tidak Dapat Dihitung Apabila Objek Saling Bertumpukan
  
## <p align="center">Penjelasan Source Code</p>
- Baris 9 Mengimpor library open-cv
- Baris 11 Menginisialisasi video capture menggunakan library cv.
- Baris 12-14 Kondisi apabila kamera tidak bisa dibuka, maka program tidak bisa membuka kamera
- Baris 17 Perulangan dengan while true artinya program akan dijalankan terus apabila frame bisa ditangkap
- Baris 19 Membaca video capture yang diambil dari variabel cap pada baris 11, dan disimpan pada variabel ret dan frame
- Baris 20 Mengubah ukuran frame dengan ukuran 400x400, dengan scale rasio x dan y = 0 menggunakan metode interpolasi inter_cubic (kualitas baik)
- Baris 23-25 Jika kondisi variabel ret tidak bisa dibaca, maka frame tidak bisa ditangkap 
- Baris 27 Mengubah frame rgb yang ditangkap oleh kamera menjadi grayscale yang disimpan 	pada variabel gray
- Baris 29 Menambahkan filter gaussian pada frame gray dengan tinggi 11 lebar 11 dengan border default nya 0 yang disimpan pada variabel blur
- Baris 31 Menerapkan filter canny dengan variabel blur treshold lower = 30 dan upper = 150, dan bukaan = 3 yang disimpan pada variabel canny
- Baris 33	Menerapkan filter dilasi pada variabel canny dengan kernel 1x1 dan iterasi = 2
- Baris 35 Mencari kontur dari dilasi yang dibuat dengan hirarki kontur ekstraksi luar dan 	metode pendekatan kontur guna menyimpan semua titik kontur
- Baris 36 Menyimpan frame yang telah diambil dengan warna rgb pada variabel rgb
- Baris 37 Menggambar semua kontur pada frame rgb yang sesuai dengan pencarian kontur variabel dan hirarki pada variabel cnt. Kontur tersebut berwarna hijau dengan 	ketebalan = 2
- Baris 39 Mendefinisikan jumlah koin pada gambar berdasarkan jumlah dari variabel cnt. Jumlah tersebut disimpan pada variabel teks
- Baris 40 Menyimpan font sans serif dengan ukuran kecil pada variabel font
- Baris 42 Menampilkan teks pada frame rgb dengan variabel teks pada koordinat tepi kiri = 10 dan koordinat tepi atas = 20, ketebalan = 1.5, teks berwarna merah dengan ketebalan = 1, jenis garis = 16 
- Baris 46 Menampilkan frame rgb dengan judul deteksi koin
- Baris 47 Menampilkan frame asli dengan judul asli
- Baris 49 Jika frame yang ditampilkan ditekan huruf q pada keyboard, maka akan frame akan 	berhenti sementara, dan jika ditekan angka 1 maka akan keluar.
- Baris 52-54 Menutup webcam atau kamera, lalu menutup semua program yang berjalan

## <p align="center">Kesimpulan dan Saran</p>
- Berdasarkan program yang telah kami buat, terlihat masih banyak kekurangan dan ketidakakuratan dalam mendeteksi jumlah koin. Oleh karena itu, dibutuhkan angle kamera yang tepat agar program dapat mendeteksi jumlah koin secara akurat.^^
- Pada penelitian selanjutnya, bisa ditambahkan fitur yang mampu untuk mendeteksi serta menghitung jumlah nominal dari objek (uang koin) tersebut. 