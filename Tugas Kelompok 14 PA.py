import mysql.connector
import pymysql
from prettytable import PrettyTable
import os
import time
from datetime import datetime

# Koneksi ke database
mydb = mysql.connector.connect(
    host="db4free.net",
    user="kelompok14",
    password="Aditya1234",
    database="database14",
)
connection = pymysql.connect(
    host="db4free.net",
    user="kelompok14",
    password="Aditya1234",
    db="database14",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        cur_node = self.head
        table = PrettyTable()
        table.field_names = ["ID", "Nama ", "Kategori", "Harga", "Stok"]
        while cur_node.next != None:
            cur_node = cur_node.next
            table.add_row(cur_node.data)
        print(table)


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [LinkedList() for _ in range(size)]

    def hash(self, key):
        # Mengembalikan indeks dalam tabel hash untuk kategori tertentu
        return hash(key) % self.size

    def search(self, key):
        # Mencari produk dengan kategori tertentu dalam tabel hash
        index = self.hash(key)
        cur = self.table[index].head.next
        lo = 0
        hi = self.table[index].length() - 1

        while lo <= hi and cur:
            pos = lo + (hi - lo) * (hash(key) - hash(cur.data[2])) // (
                hash(self.table[index].head.next.data[2])
                - hash(self.table[index].head.next.next.data[2])
            )
            if pos < lo or pos > hi:
                break
            cur = self.table[index].head.next
            for i in range(pos):
                cur = cur.next
            if cur.data[2] == key:
                yield cur.data
                break
            elif hash(cur.data[2]) < hash(key):
                lo = pos + 1
            else:
                hi = pos - 1


def kelola_produk():
    while True:
        print("\n===== KELOLA PRODUK =====")
        print("1. Tambah produk")
        print("2. Hapus produk")
        print("3. Perbarui produk")
        print("4. Kembali ke menu utama")

        try:
            pilihan = int(input("Pilih menu: "))
            if pilihan == 1:
                TambahProduk()
            elif pilihan == 2:
                HapusProduk()
            elif pilihan == 3:
                PerbaruiProduk()
            elif pilihan == 4:
                break
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Mohon masukkan angka.")


def produk():
    mycursor = mydb.cursor()

    # Check if table 'produk' is empty
    mycursor.execute("SELECT COUNT(*) FROM produk")
    produk_count = mycursor.fetchone()[0]
    if produk_count == 0:
        print("Tabel 'produk' masih kosong.")
        exit()

    while True:
        print("\n===== MENU =====")
        print("Pilih aksi:")
        print("1. Lihat semua produk")
        print("2. Beli Produk")
        print("4. Kembali ke menu utama")
        try:
            pilihan = int(input("Masukkan pilihan (1/2/3): "))
            if pilihan == 1:
                os.system("cls")
                LihatProduk()
            elif pilihan == 2:
                try:
                    produk1()
                    kode_produk = input("Masukkan kode produk: ")
                    jumlah_beli = int(input("Masukkan jumlah pembelian: "))

                    # cek apakah produk tersedia di database
                    mycursor.execute(
                        "SELECT * FROM produk WHERE id = %s", (kode_produk,)
                    )
                    result = mycursor.fetchone()

                    if result == None:
                        print("Produk tidak tersedia.")
                    else:
                        stok_produk = result[4]

                        # cek apakah stok produk mencukupi
                        if stok_produk < jumlah_beli:
                            print("Stok produk tidak mencukupi.")
                        else:
                            harga_produk = result[3]
                            total_harga = harga_produk * jumlah_beli

                            # kurangi jumlah stok produk di database
                            mycursor.execute(
                                "UPDATE produk SET stok_produk = stok_produk - %s WHERE id = %s",
                                (jumlah_beli, kode_produk),
                            )
                            mydb.commit()

                            # simpan transaksi ke dalam tabel transaksi
                            waktu = datetime.now()
                            produk_id = result[0]
                            mycursor.execute(
                                "INSERT INTO transaksi (waktu, nama_produk, produk_id, jumlah) VALUES (%s, %s, %s, %s)",
                                (waktu, result[1], produk_id, jumlah_beli),
                            )
                            mydb.commit()

                            # print struk
                            print("========== STRUK PEMBELIAN ==========")
                            print("Jumlah item:", jumlah_beli)
                            print("Total harga:", total_harga)
                            print("=====================================")
                            # membuka file untuk menulis struk
                            with open("struk_pembelian.txt", mode="w") as file:
                                # menulis struk ke dalam file
                                file.write("========== STRUK PEMBELIAN ==========\n")
                                file.write("Jumlah item: {}\n".format(jumlah_beli))
                                file.write("Total harga: Rp {}\n".format(total_harga))
                                file.write("=====================================\n")
                                time.sleep(5)
                                os.system("cls")
                            print(
                                "Produk berhasil dibeli. Total harga: Rp", total_harga
                            )
                            os.system("cls")
                            break
                except ValueError:
                    print("Mohon masukkan angka untuk jumlah pembelian.")

            elif pilihan == 4:
                break
            else:
                print("Pilihan tidak valid.")

        except ValueError:
            print("Mohon masukkan angka.")


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][3] < right_half[j][3]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def TambahProduk():
    try:
        mycursor = mydb.cursor()
        os.system("cls")
        # Meminta input dari pengguna
        nama_produk = input("Masukkan nama produk: ")
        kategori_produk = input("Masukkan kategori produk: ")
        harga_produk = int(input("Masukkan harga produk: "))
        if harga_produk < 0:
            raise ValueError("Harga produk tidak boleh negatif.")
        stok_produk = int(input("Masukkan stok produk: "))
        if stok_produk < 0:
            raise ValueError("Stok produk tidak boleh negatif.")
        sql = "INSERT INTO produk (nama_produk, kategori_produk, harga_produk, stok_produk) VALUES (%s, %s, %s, %s)"
        val = (nama_produk, kategori_produk, harga_produk, stok_produk)
        mycursor.execute(sql, val)
        mydb.commit()
        print(f"Produk '{nama_produk}' berhasil ditambahkan ke database.")
    except ValueError as error:
        print(f"Input yang dimasukkan tidak valid: {error}")
    except mysql.connector.Error as error:
        print(f"Terjadi kesalahan pada database: {error}")


def HapusProduk():
    try:
        mycursor = mydb.cursor()

        # Meminta input dari pengguna
        Id = input("Masukkan id produk: ")

        # Menghapus produk dari database
        mycursor.execute("DELETE FROM produk WHERE id=%s", (Id,))
        mydb.commit()

        print(f"Produk dengan kode '{Id}' berhasil dihapus dari database.")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")


def PerbaruiProduk():
    try:
        mycursor = mydb.cursor()
        os.system("cls")
        # Meminta input dari pengguna
        Id = input("Masukkan id produk: ")
        print("Pilih data produk yang ingin diubah:")
        print("1. Nama produk")
        print("2. Kategori produk")
        print("3. Harga produk")
        print("4. Stok produk")
        option = input("Masukkan pilihan (1/2/3/4): ")

        # Validasi pilihan
        while option not in ["1", "2", "3", "4"]:
            option = input("Masukkan pilihan yang valid (1/2/3/4): ")

        # Menentukan field yang akan diubah
        if option == "1":
            field = "nama_produk"
        elif option == "2":
            field = "kategori_produk"
        elif option == "3":
            field = "harga_produk"
        elif option == "4":
            field = "stok_produk"

        value = input(f"Masukkan {field} baru: ")

        # Memperbarui produk di database
        mycursor.execute(f"UPDATE produk SET {field} = %s WHERE id=%s", (value, Id))
        mydb.commit()

        print(f"Produk dengan kode '{Id}' berhasil diperbarui.")
    except Exception as e:
        print("Terjadi error:", e)


def kelola_kasir():
    while True:
        os.system("cls")
        print("\n===== KELOLA KASIR =====")
        print("1. Tambah akun kasir")
        print("2. Hapus akun kasir")
        print("3. Kembali ke menu utama")

        try:
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                tambah_kasir()
            elif pilihan == "2":
                hapus_kasir()
            elif pilihan == "3":
                break
            else:
                raise ValueError(
                    "Pilihan tidak valid. Silakan pilih antara 1, 2, atau 3."
                )
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")


def tambah_kasir():
    try:
        mycursor = mydb.cursor()

        # Meminta input dari pengguna
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        # Menambahkan akun kasir ke database
        mycursor.execute(
            "INSERT INTO users (username, password, privilege) VALUES (%s, %s, 'kasir')",
            (username, password),
        )
        mydb.commit()

        print(f"Akun kasir '{username}' berhasil ditambahkan ke database.")
    except:
        print("Terjadi kesalahan saat menambahkan akun kasir. Silakan coba lagi.")


def hapus_kasir():
    try:
        mycursor = mydb.cursor()

        # Meminta input dari pengguna
        username = input("Masukkan username: ")

        # Menghapus akun kasir dari database
        mycursor.execute("DELETE FROM users WHERE username=%s", (username,))
        mydb.commit()

        print(f"Akun kasir '{username}' berhasil dihapus dari database.")
    except:
        print("Terjadi kesalahan saat menghapus akun kasir. Silakan coba lagi.")


def LihatProduk():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM produk")
    result = mycursor.fetchall()
    if not result:
        print("Tidak ada produk yang tersedia.")
        return
    else:
        linked_list = LinkedList()
        for item in result:
            linked_list.append(item)
        linked_list.display()


def produk1():
    LihatProduk()
    mycursor = mydb.cursor()

    # Meminta input dari pengguna
    pilih_kategori = input(
        "Apakah anda ingin mencari produk berdasarkan kategori? (Y/N): "
    )

    # Jika pengguna memilih mencari produk berdasarkan kategori
    if pilih_kategori.upper() == "Y":
        print("Daftar kategori produk: ")
        print(
            "1. Makanan\n2. Minuman\n3. Alat Tulis Kantor\n4. Peralatan Rumah Tangga\n5. Obat - Obatan"
        )

        # Meminta input kategori yang dicari dari pengguna
        kategori = input("Masukkan nomor kategori produk: ")

        # Mengubah nomor kategori menjadi nama kategori
        if kategori == "1":
            nama_kategori = "Makanan"
        elif kategori == "2":
            nama_kategori = "Minuman"
        elif kategori == "3":
            nama_kategori = "Alat Tulis Kantor"
        elif kategori == "4":
            nama_kategori = "Peralatan Rumah Tangga"
        elif kategori == "5":
            nama_kategori = "Obat - Obatan"
        else:
            print("Nomor kategori tidak valid.")
            return

        # Menampilkan produk dengan kategori yang sama menggunakan query SQL
        mycursor.execute(
            "SELECT * FROM produk WHERE kategori_produk=%s",
            (nama_kategori,),
        )
        result = mycursor.fetchall()

        # Menampilkan hasil pencarian produk ke layar
        if not result:
            print(f"Tidak ada produk dengan kategori '{nama_kategori}'")
        else:
            pilih_sort = input(
                "Apakah anda ingin mengurutkan hasil pencarian berdasarkan harga? (Y/N): "
            )
            if pilih_sort.upper() == "Y":
                merge_sort(result)  # mengurutkan hasil pencarian berdasarkan harga
            table = PrettyTable()
            table.field_names = ["ID", "Nama ", "Kategori", "Harga", "Stok"]
            for item in result:
                table.add_row(item)
            print(table)

    # Jika pengguna tidak ingin mencari produk berdasarkan kategori
    elif pilih_kategori.upper() == "N":
        mycursor.execute("SELECT * FROM produk")
        result = mycursor.fetchall()

        # Meminta input pengguna untuk mengurutkan semua produk berdasarkan harga
        pilih_sort = input(
            "Apakah anda ingin mengurutkan semua produk berdasarkan harga? (Y/N): "
        )
        if pilih_sort.upper() == "Y":
            merge_sort(result)
            table = PrettyTable()
            table.field_names = ["ID", "Nama ", "Kategori", "Harga", "Stok"]
            for item in result:
                table.add_row(item)
            print(table)  # mengurutkan semua produk berdasarkan harga
        # Menampilkan semua produk ke layar
        if not result:
            print("Tidak ada produk yang tersedia.")
        else:
            table = PrettyTable()
            table.field_names = ["ID", "Nama ", "Kategori", "Harga", "Stok"]
            for item in result:
                table.add_row(item)
            print(table)

    # Jika input pengguna tidak valid
    else:
        print("Input tidak valid.")


def transaksi():
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="kelompok14",
        password="Aditya1234",
        database="database14",
    )
    # Buat cursor untuk melakukan query
    mycursor = mydb.cursor()

    # Lakukan query
    mycursor.execute("SELECT * FROM transaksi")

    # Ambil semua hasil query
    result = mycursor.fetchall()

    # Tampilkan hasil menggunakan PrettyTable
    table = PrettyTable()
    table.field_names = ["ID", "Waktu", "Nama Produk", "Produk ID", "Jumlah"]
    for item in result:
        table.add_row(item)
    print(table)


def kasir():
    while True:
        print("========== KASIR ==========")
        print("1. Transaksi Penjualan")
        print("2. Daftar Produk")
        print("0. Kembali ke Menu Utama")
        try:
            pilihan = int(input("Masukkan pilihan anda: "))
        except ValueError:
            print("Mohon masukkan angka saja.\n")
            continue
        if pilihan == 1:
            transaksi()
        elif pilihan == 2:
            produk1()
        elif pilihan == 0:
            return

        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")


def kelola_produk1():
    while True:
        print("========== ADMIN ==========")
        print("1. Kelola produk")
        print("2. Kelola kasir")
        print("3. Kembali ke menu utama")
        try:
            pilihan = int(input("Masukan pilihan anda: "))
        except ValueError:
            print("Mohon masukkan angka saja.")
            continue

        if pilihan == 1:
            kelola_produk()
        elif pilihan == 2:
            kelola_kasir()
        elif pilihan == 3:
            return
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")


def menu(user):
    if user["privilege"] == "admin":
        kelola_produk1()
    elif user["privilege"] == "kasir":
        kasir()


def login():
    connection = pymysql.connect(
    host="db4free.net",
    user="kelompok14",
    password="Aditya1234",
    db="database14",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
    )
    while True:
        username = input("Username: ")
        password = input("Password: ")

        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE username=%s AND password=%s"
            cursor.execute(sql, (username, password))
            user = cursor.fetchone()

            if user:
                print("Login berhasil!")
                return user
            else:
                print("Username atau password salah!")


def main():
    user = login()
    menu(user)


def menu_login():
    os.system("cls")
    print("==Selamat datang di program supermarket aldous mart!==")
    print("Silakan pilih opsi:")
    print("1. Admin")
    print("2. Kasir")
    print("3. Pembeli")
    print("0. Keluar")
    try:
        choice = int(input("Masukkan pilihan Anda: "))
        return str(choice)
    except ValueError:
        print("Masukkan angka saja.")
        return "-1"


while True:
    choice = menu_login()
    if choice == "1" or choice == "2":
        if __name__ == "__main__":
            main()
    elif choice == "3":
        os.system("cls")
        produk()
    elif choice == "0":
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
