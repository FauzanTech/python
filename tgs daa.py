# Program untuk menyelesaikan tugas 1 DAA nomor 1
# a. Tugas dikerjakan menggunakan pendekatan Exhaustive Search, yaitu dengan melakukan
# Pengurutan terhadap semua bilangan dari yang terkecil ke terbesar
# Setelah itu, otomatis bilangan yang berada pada paling kiri adalah bilangan terkecil
# dan bilangan pada paling kanan adalah bilangan paling besar
# Jika terdapat bilangan 0 maka akan di hapus

# b. Penerapan
def cariPecahanTerbesar(arr):
    arr.sort()

    jumlah_angka_nol = arr.count(0)
    while jumlah_angka_nol:
        arr.remove(0)
        jumlah_angka_nol-=1

    # print(arr)
    min = arr[0]
    max = arr[-1]
    # c. Hasil
    print(f"{max}/{min} = {max/min}")

input_angka = list(map(int, input("Masukkan angka: ").split()))
cariPecahanTerbesar(input_angka)

# d. Penjelasan
# Berdasarkan arti dari Exhaustive Search yakni pencarian menyeluruh maka kita harus mencari sesuatu tanpa melewati
# satu itempun. Dikarenakan kita menggunakan bahasa python yang lebih menguntungkan menurut kami karena tipe data list yang tersedia.
# Ada 2 cara yang terpikirkan oleh kami yang satu langsung menggunakan method max dan min kemudian yang kedua
# Mengurutkan bilangan dari terkecil ke terbesar kemudian mengambil nilai paling kiri(terkecil) dan
# paling kanan(terbesar). Untuk bilangan nol apabila ada maka tinggal di hapus saja.

# e. kekurangan
# Kekurangannya mungkin terletak pada kompleksitas waktu yang digunakan mengingat 
# kita menggunakan exhaustive search yang berarti pencarian yang kita lakukan harus secara menyeluruh
# Mungkin kalau angka yg kita cari berjumlah tidak terlalu banyak maka tidak apa, tetapi ketika jumlah angka yang akan ditelusuri sangat banyak
# barulah terasa kekurangan ini. 