# P1_Komnum_D10
Praktikum 1 mengenai implementasi Metode Bolzano terhadap suatu akar persamaan

## Anggota
|     | Nama                              | NRP        | Jobdesk                                   |
| --- | --------------------------------- | ---------- | ----------------------------------------- |
| 1   | Rizky Alifiyah Rahma              | 5025211208 | Membuat file codingan dan dokumen laporan |
| 2   | Muhammad Naufal Fawwaz Ramadhan   | 5025211223 | Mendemokan program                        |

## Penjelasan
- ### Fungsi yang digunakan

   | Nama Fungsi        | Penjelasan Singkat         |          
   ---------------------| -------------------------- |
   def clear()          | Berfungsi untuk membersihkan layar dari semua teks yang telah ditulis saat berganti section |
   def error()          | Berfungsi untuk memberitahukan user saat memasukkan persamaan yang salah atau tidak sesuai format |
   def f(x,p)           |   Terdapat fungsi bawaan yaitu fungsi `eval()` yang berfungsi untuk menyelesaikan operasi matematika pada bilangan bulat atau float dalam bentuk string |
   def persamaan()      | Berfungsi untuk merubah notasi ^ menjadi notasi pangkat yang ada di dalam persamaan |
   def grafik()         | Dalam fungsi ini digunakan library `matplotlib` yang berfungsi dalam penggambaran grafik beserta titik uji cobanya |
   def bolzano()        | Berfungsi untuk mencari akar dalam suatu persamaan menggunakan metode bolzano. Dengan memasukkan titik bawah dan titik atas (x1 dan x2) selama `f(x1)*f(x2) >= 0` dan `1 < abs(fx3) < 100`, ditemukan akar persamaan (x3) yang akan dimasukkan kedalam fungsi persamaan (f(x3)). Dari x3 dan f(x3) akan menghasilkan titik-titik di sepanjang kurva |

   #### Penjelasan lanjutan fungsi bolzano()
   Ada 2 kondisi yang mungkin terjadi:
   1. Jika `f(x1)*f(x2) < 0`, maka:
      - program mengeluarkan output `belum memenuhi syarat`
      - mengulangi proses input `x1` dan `x2`hingga syarat terpenuhi
   
   3. Jika `f(x1)*f(x2) >= 0`, maka:
      - program mengeluarkan output `sudah memenuhi syarat`
      - lanjut mencari `x3` dan `f(x3)`
      - set nilai `x3` menjadi `(x1 + x2)/2`
      - menghitung `f(x3)`
</br>

- ### Alur Program
   1. User melakukan input pembulatan, taraf error, titik bawah (x1), dan titik atas (x2) pada fungsi `main()`
   2. Program mengecek apakah terdapat lebih dari 2 argumen atau tidak
      - Jika iya, user akan keluar dari program
      - Jika tidak, lanjut pengecekan apakah terdapat variabel selain x atau tidak
         - Jika iya, user akan keluar dari program
         - Jika tidak, lanjut ke metode bolzano
   3. Pada fungsi `bolzano()`, rekursi akan berjalan selama memenuhi syarat `f(x1)*f(x2) >= 0` dan `1 < abs(fx3) < 100`
   4. Jika rekursi berhenti, program akan menampilkan tabel data dan grafik
</br>

## Preview Output
![Screenshot 2022-10-29 012639](https://user-images.githubusercontent.com/90395116/198706935-75b63981-5fa8-4156-a95e-774926f0c2ee.png)
![Figure_1](https://user-images.githubusercontent.com/90395116/198706962-ca6eff47-9b44-48d6-967d-5afff1afe330.png)
