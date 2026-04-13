![Text Alt](GambarAppy1.png)
![Text Alt](GambarAppy2.png)

(Baris 1-4)
*1:* Memanggil library `requests` supaya aplikasi bisa "berselancar" ke internet untuk cari data.*2:* Memanggil fitur Flask untuk bikin website, menampilkan halaman (`render_template`), dan membaca input user (`request`).
*4:* Membuat "kerangka" aplikasi web Anda dengan nama `app`.

Bagian 2: Fungsi Pengambil Harga Dollar (Baris 6-16)
Fungsi ini bertugas mengecek harga USD ke IDR yang paling baru.
*6-11:* Program mencoba (`try`) menyambung ke website penyedia data (API). Jika internet nyala, aplikasi akan mengambil data harga terbaru.
*13:* Mengambil angka spesifik untuk Rupiah (`IDR`) dari tumpukan data yang didapat.
*14-16: Jika terjadi masalah (misal internet mati), program akan masuk ke rencana cadangan (`except`) dan memakai angka **16.200** sebagai patokan sementara.

Bagian 3: Logika Halaman Utama (Baris 18-32)
Ini adalah bagian yang mengatur apa yang muncul di layar HP/Laptop user.
*18:* Menentukan alamat website utama (`/`) dan mengizinkan pengiriman data (POST).
*19-21:* Menyiapkan variabel kosong untuk menampung hasil hitungan nanti.
*22:* Memanggil harga Dollar terbaru (dari fungsi di atas).
*23:* Mengecek: "Apakah user sedang menekan tombol Hitung?"
*24-26:*Jika iya, ambil angka USD yang diketik user, lalu kalikan dengan harga kurs: **Total = USD × Kurs**.
*28:* Mengubah format angka. Misalnya dari format komputer `15000.5` menjadi format kita `15.000,50` agar enak dibaca.
*29-30:* Jika user salah ketik (misal mengetik huruf, bukan angka), munculkan pesan "Input tidak valid".
*32:* Mengirim hasil hitungan tadi ke file `index.html` supaya tampil di layar.

# Bagian 4: Menjalankan Program (Baris 34-35)
*34-35:* Perintah untuk menyalakan mesin website. Mode `debug=True` artinya jika Anda mengubah kode, website akan otomatis terupdate tanpa harus dimatikan manual.

---

![Text Alt](GambarKalkulator.png)
 http://127.0.0.1:5000

 *1. Cara Kerjanya (Alur)*
1. *Ambil Data:* Aplikasi otomatis "menghubungi" website penyedia kurs mata uang untuk mencari harga $1$ USD ke Rupiah paling terbaru (misal: **Rp 17.090**).
2. *Terima Input:** Kamu memasukkan jumlah Dollar yang ingin dihitung ke kolom putih..  
3. *Proses Hitung:* Saat tombol diklik, aplikasi mengalikan **[Angka Kamu]** $\times$ 
4. *[Harga Kurs]*.
5.  *Tampilkan:* Hasilnya dimunculkan kembali ke layar dengan format rupiah yang rapi (menggunakan titik dan koma).

*2. Fungsi Bagian di Layar*
*Header:* Menunjukkan harga Dollar detik ini (real-time).
*Kolom Input:* Tempat kamu memasukkan angka (hanya angka, jika huruf akan error).
*Tombol Pink:* Pemicu agar mesin Python di belakang layar mulai menghitung.
*3. Keunggulan*
*Akurat:* Harga tidak dikarang sendiri, tapi ambil dari data bank dunia.
*Tahan Error:* Jika internetmu mati, ia sudah punya angka "cadangan" agar tetap bisa berfungsi.
*User Friendly:* Tampilan didesain cantik (pakai CSS) agar enak dilihat dan mudah dipakai.

---

