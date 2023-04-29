# TugasKelompok14

**Project Title: Aldous Mart (Supermarket)**
**Deskripsi Program**
Program ini merupakan sebuah sistem manajemen untuk supermarket yang dirancang dengan tujuan memfasilitasi pengguna dalam melakukan transaksi. Dalam program ini, pengguna memiliki kemampuan untuk mengelola stok barang, memproses penjualan, mencetak riwayat pembelian atau invoice secara otomatis, dan mengelola kasir. Dengan fitur-fitur yang disediakan, program ini diharapkan dapat meningkatkan efisiensi dan efektivitas proses bisnis di dalam supermarket.
Dalam pemrograman, kita dapat menggunakan konsep `Class Node` sebagai kerangka untuk membuat objek struktur data `Linked List`. Struktur data ini terdiri dari objek-objek `Node` yang terhubung satu sama lain melalui referensi. Kita juga dapat menggunakan `Class Linked List` sebagai struktur data utama untuk mengelola kumpulan objek `Node` dalam linked list tersebut. 
Selain itu, untuk mempercepat pencarian dan pengambilan data dari kumpulan data yang besar, kita dapat menggunakan `Class Hash Table`. Struktur data ini memungkinkan kita untuk menyimpan data dalam bentuk pasangan "kunci-nilai" (key-value pair), dengan menggunakan algoritma hash untuk menentukan lokasi penyimpanan data dalam tabel. Dengan demikian, kita dapat menggabungkan konsep `Class Node` dan `Class Linked List` untuk membentuk struktur data linked list, serta mengombinasikannya dengan `Class Hash Table` untuk mempercepat pencarian dan pengambilan data pada linked list.
Dalam penerapannya, program ini mendukung sistem login multiuser, di mana pengguna dapat masuk sebagai Admin untuk mengelola produk dan kasir, sebagai Kasir untuk melakukan transaksi penjualan dan melihat daftar produk, atau sebagai Pembeli untuk melihat semua daftar produk, mencari produk berdasarkan kategori, dan melakukan pembelian.

FUNGSIONALITAS 

-Admin telah Memiliki akun yang dapat digunakan langsung di dalam program

-Admin dapat mengelola produk seperti Tambah Produk, Hapus Produk, dan Perbarui Produk

-Admin dapat Mengelola Kasir seperti Menambah kan Kasir baru atau Menghapus kasir tersebut

-Kasir telah mempunyai akun yang dapat di jalankan di dalam program seperti admin

-Kasir dapat mengecek history Transaksi Penjualan 

-Kasir Dapat Melihat daftar produk dan bisa melihat detail seperti Lihat semua produk atau Melihat berdasarkan Kategori

-Pembeli dapat melihat Daftar produk dan membeli produk

Struktur Project:
A.	Import Library:
Program ini menggunaka beberapa library diantaranya ialah:
	Mysql.connector 
Adalah sebuah modul pada python yang digunakan untuk menghubungkan program python pada database MySQL. Dnegan menggunakan modul ini, pengguna dapat melakukan operasi membaca,menulis,mengubah dan menghapus data dari MySQl melalui program python.
	Pymysql
Sama seperti mysql.connector tadi, modul ini digunakan untuk menghubungkan program python pada database MySQL.
	PrettyTable
Adalah sebuah Library yang digunakan untuk membuat table yang mudah di baca oleh manusia.
	Time 
Time merupakan modul yang digunakan untuk mengakses fungsi-fungsi terkait waktu, seperti menunda eksekusi program untuk beberapa waktu tertentu.
B.	Class Node
Class Node yang merupakan suatu kerangka yang digunakan dalam membuat objek struktur data Linked List. Dalam class Node terdapat def __init__, yang berfungsi untuk menginisialisasi objek yang dibuat dengan nilai-nilai awal tertentu.
C.	Class LinkedList
Class Linked List yang merupakan struktur data yang terdiri dari objek Node yang terhubung satu sama lain. Dalam Class LinkedList terdapat beberapa def yaitu:
•	Def __init__, yang berfungsi untuk menginisialisasi objek yang dibuat dengan nilai-nilai awal tertentu.
•	Def Append, yang berfungsi untuk menambah sebuah elemen baru.
•	Def Length, digunakan untuk menghitung jumlah node atau elemen yang terdapat pada linked list.
•	Def Display, digunakan untuk menampilkan atau mengakses data atau informasi dari objek yang dibuat dari class trersebut. 

D.	Class HashTable
Class Hash Table yang merupakan struktur data yang di gunakan dalam pemrograman untuk mempercepat pencarian dan pengambilan data dari kumpulan data yang besar. Pada class Hashtable terdapat beberapa def yaitu:
•	Def __init__, yang berfungsi untuk menginisialisasi objek yang dibuat dengan nilai-nilai awal tertentu.
•	Def Hash, berfungsi untuk mengembalikann nilai indeks dari suatu kunci pada hash table. 
•	Def Search, untuk mencari dan mengembalikan data yang diinginkan dari suatu kumpulan data yang disimpan dalam struktur data tertentu.  Pada program ini kami menggunakan Interpolation search. Interpolation search adalah algoritma pencarian data dalam suatu array atau list yang telah terurut. Teknik pencariannya menggunakan formula matematika untuk memperkirakan posisi data yang di cari berdasarkan nilai maksimum dan minimum pada list. Sehingga mempercepat proses pencarian data. 

E.	Def kelola_produk
Adalah sebuah fungsi untuk mengelola data produk. Def ini akan menampilkan menu pada layar, seperti pilihan untuk menambahkan produk baru, menghapus produk, mengubah produk dan kembali ke menu utama. 

F.	Def Merge_sort
adalah algoritma pengurutan yang efisien dan cepat. Cara kerjanya adalah dengan membagi array yang akan di urutkan menjadi 2 bagian, lalu melakukan pengurutan secara rekrusif pada kedua bagian tersebut. Setelah kedua bagian sudah terurut maka bagian tadi di gabung kembali menjadi satu array. 

G.	Def TambahProduk
Digunakan untuk menambahkan produk baru ke dalam database. User di minta untuk memasukkan nama produk,kategori produk,harga produk dan stok produk. Kemudian data disimpan ke dalam database. 

H.	Def HapusProduk
Digunakan untuk menghapus data produj dari database. Fungsinya akan meminta input dari pengguna berupa id produk yang akan di hapus, kemudian menghapus produk tersebut dari database. 

I.	Def PerbaruiProduk
Digunakan untuk memperbarui data produk yang ada di databse. User diminta untuk menginputkan id produk dan memilih data produk mana yang ingin di ubah. Kemudian user diminta untuk memasukkan produk baru.

J.	Def kelola_kasir
Untuk menampilkan menu kelola kasir, dimana user dapat memilih untuk menambah atau menghapus akun kasir, atau kembali ke menu utama. 

K.	Def tambah_kasir
Untuk menambahkan akun kasir baru ke database. Saat fungsi dijalankan, pengguna diminta untuk memasukkan username dan password untuk akun kasir baru. 

L.	Def hapus_kasir
Berfungsi untuk menghapus akun kasir pada database. User diminta untuk memasukkan username dari akun kasir yang di hapus, kemudian fungsi akan mencari dan menghapus akun kasir tersebut dari database. 

M.	Def LihatProduk
Digunakan untuk menampilkan daftar produk yang tersimpan dalam database. Pertama, fungsi akan melakukan koneksi ke database dan mengambil semua data produk dari table produk menggunakan perintah SQL SELECT. 

N.	Def transaksi
Untuk menampilkan seluruh transaksi yang terjadi pada database dengan menggunakan modul mysql.connector untuk mengakses database. 
O.	Def kasir
Bagian dari program kasir yang memiliki beberapa opsi untuk dipilih oleh pengguna. Opsi pertamam untuk melakukan transaksi penjualan, opsi kedua untuk melihat daftar produk yang tersedia dan opsi ketiga untuk kembali ke menu utama.

P.	Def menu
Untuk menampilkan menu yang berbeda tergantung pada user admin atau kasir. Jika user adalah admin, maka akan memanggil fungsi kelola produk dan mengizinkan user untuk mengelola produk. Jika user sebagai kasir maka akan memanggil fungsi kasir yang memungkinkan pengguna untuk melakukan transaksi penjualan.

Q.	Def login
Memungkinkan user untuk login dengan memasukkan username dan password. Jika username dan password benar maka program akan memberikan akses pengguna dan mencetak pesan “Login Berhasil!”. Jika salah, maka program akan mencetak pesan “Username atau Password salah!” dan meminta user untuk memasukkan username dan password lagi. 

R.	Def main 
Adalah fungsi utama yang akan dijalankan ketika program dijalankan.  Fungsi ini akan memanggil dua fungsi lainnya yaitu def login dan def menu. 

S.	Def menu_login
Untuk menampilkan pilihan menu login, yaitu sebagai admin,kasir, atau pembeli. Program akan terus menampilkan menu login apabila user memilih untuk keluar dengan memilih opsi 0. 

CARA PENGGUNAAN 


Menu Tampilan Awal
Pada menu tampilan awal terdapat 4 pilihan yaitu yang pertama login Admin, yang kedua login Kasir yang ketiga pembeli yang terakhir adalah Keluar:
1. Pilih angka "1" jika ingin masuk sebagai Admin maka akan di tampilkan menu admin
2. Pilih angka "2" jika ingin masuk sebagai Kasir maka akan di tampilkan menu Kasir
3. Pilih angka "3" jika ingin masuk sebagai Pembeli maka akan di tampilkan menu Pembeli
4.Pilih angka "0" jika ingin Keluar

Login Admin
Pada Login Admin user harap memasukan username dan password yang sudah di sediakan yaitu username = Admin Password = Admin.Setelah login maka akan di tampilkan 3 opsi yaitu Kelola Produk, Kelola Kasir dan Kembali ke menu awal                                                                                                                                                              
1.Pertama menu Kelola produk pada menu akan ditampilkan 4 opsi yaitu: 
1. Tambah produk
2. Hapus produk
3. Perbarui produk
4. Kembali ke menu utama
Jika memilih opsi 1 maka user dapat menambkan produk sesuai kategori produk dan dapat menentukan Harga dan Stok produk tersebut
Jika memilih opsi 2 maka user dapat menghapus produk yang di ingginkan dengan id produk yaitu nama barang tersebut
Jika memilih opsi 3 maka user dapat Perbarui produk yang ingin di ingginkan dengan memasukan nama barang tersebut maka user dapat mengubah nama produk, kategori produk, harga produk, dan stok produk
Jika memilih opsi 4 maka user akan kembali ke menu utama admin
2.Kedua menu Kelola Kasir pada menu akan di tampilkan 3 opsi yaitu:
1. Tambah akun kasir
2. Hapus akun kasir
3. Kembali ke menu utama
Jika memilih opsi 1 maka user bisa menambahkan kasir baru dengan menambahkan username dan password jika sudah menambahkan otomatis sudah masuk di database
Jika memilih opsi 2 maka user bisa menghapus akun kasir dengan memasukan nama username kasir yang ingin di hapus maka otomatis terhapus di database
Jika memilih opsi 3 maka user akan kembali ke menu utama
3.Ketiga menu Kembali ke menu utama maka user akan kembali ke menu awal

Login Kasir
Pada Login KAsir user harap memasukan username dan password yang sudah di sediakan yaitu username = Kasir Password = Kasir.Setelah login maka akan di tampilkan 3 opsi yaitu Transaksi Penjualan, Daftar Produk dan Kembali ke menu awal
1.Pertama di menu Transaksi Penjualan dapat melihat History database yang telah melakukan pembelian dan dapat melihat ID produk, Waktu, Jumlah dan Nama Produk
2.Kedua di Menu Daftar Produk maka akan di tampilkan 3 opsi yaitu Lihat semua Produk, Cari produk Berdasrkan Kategori dan Kembali ke menu utama
-Opsi 1 yaitu lihat semua produk dapat melihat semua produk dan bisa di urutkan sesuai harga
-Opsi 2 yaitu Mencari Produk berdasarkan Kategori yang sudah di buat
-Opsi 3 yaitu Kembali ke menu utama
3.Ketiga yaitu Kembali Ke menu utama

Login Pembeli
Pada Login Pembeli maka akan di tampilkan 3 opsi yaitu Lihat daftar produk, Beli Produk, dan Kembali Ke menu utama
1.Pertama Lihat daftar produk pembeli dapat melihat Daftar-daftar produk yang di Jual di Supermarket. Tertera juga Harga Produk Tersebut dan kode produk jika ingin membeli
2.Kedua Beli Produk maka pembeli dapat memasukan kode produk dan ingin membeli berapa stok dan akan di cetak struk setelah membeli dan melihat total harga produk yang di beli
3.Ketiga kembali ke menu utama user akan kembali ke menu awal program
