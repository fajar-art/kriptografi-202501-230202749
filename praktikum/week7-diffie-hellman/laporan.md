# Laporan Praktikum Kriptografi

Minggu ke-: X  
Topik: [Diffie-Hellman Key Exchange]  
Nama: [Fajar Saputro]  
NIM: [230202749]  
Kelas: [5IKRB]

---

## 1. Tujuan

Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).

---

## 2. Dasar Teori

(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll. )

---

## 3. Alat dan Bahan

(- Python 3.x

- Visual Studio Code / editor lain
- Git dan akun GitHub
- Library tambahan (misalnya pycryptodome, jika diperlukan) )

---

## 4. Langkah Percobaan

(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:

1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code

(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode

#diffie hellman
import random

# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)


#MITM (Man in the Middle)
#simulasi man in the middle attack pada diffie-hellman
import random

# parameter umum (public)
p = 23
g = 5

# Private keys Alice dan Bob
a = random.randint(1, p-1)
b = random.randint(1, p-1)

# Eve juga memilih private key sendiri
e = random.randint(1, p-1)

# Public keys normal (tanpa serangan)
A_real = pow(g, a, p)  # Alice
B_real = pow(g, b, p)  # Bob

# Eve mencegat dan mengganti public key
A_fake_for_B = pow(g, e, p)  # Dikirim ke Bob seolah dari Alice
B_fake_for_A = pow(g, e, p)  # Dikirim ke Alice seolah dari Bob

# Alice menghitung shared key dgn key palsu dari Eve
shared_A_E = pow(B_fake_for_A, a, p)

# Bob menghitung shared key dgn key palsu dari Eve
shared_B_E = pow(A_fake_for_B, b, p)

# Eve menghitung kedua shared key
eve_with_A = pow(A_real, e, p)
eve_with_B = pow(B_real, e, p)

print("=== TANPA SERANGAN ===")
print("Public A:", A_real)
print("Public B:", B_real)
print()

print("=== DENGAN SERANGAN MITM OLEH EVE ===")
print("Kunci Alice-Eve :", shared_A_E)
print("Kunci Bob-Eve   :", shared_B_E)
print("Kunci Eve dengan Alice :", eve_with_A)
print("Kunci Eve dengan Bob   :", eve_with_B)


```

)

---

## 6. Hasil dan Pembahasan

(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).

- Berikan tabel atau ringkasan hasil uji jika diperlukan.
- Jelaskan apakah hasil sesuai ekspektasi.
- Bahas error (jika ada) dan solusinya.

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi Diffie Hellman](screenshots/Run_Diffie.png)
![Hasil Eksekusi Simulasi MITM](screenshots/mim.png)

---

## 7. Jawaban Pertanyaan

(Jawab pertanyaan diskusi yang diberikan pada modul.

- Pertanyaan 1: Mengapa Diffie-Hellman memungkinkan pertukaran kunci di saluran publik?
  Karena protokol ini hanya bertukar nilai publik (p, g, dan public key masing-masing), sementara kunci rahasia tetap tersimpan di pihak masing-masing. Proses perhitungan kunci bersama memanfaatkan operasi exponential modulo (Discrete Logarithm Problem) yang secara matematis sangat sulit dibalik.
  Artinya, meskipun penyerang melihat semua data yang ditransmisikan secara publik, ia tidak dapat menghitung kunci rahasia bersama dengan mudah.
- Pertanyaan 2: Apa kelemahan utama protokol Diffie-Hellman murni?
  Kelemahan paling kritis adalah tidak ada autentikasi.
  Penyerang dapat melakukan:

MITM (Man-In-The-Middle Attack):
Penyerang memalsukan public key saat pertukaran, sehingga:

1. Alice berbagi kunci dengan penyerang
2. Bob berbagi kunci dengan penyerang
3. Alice dan Bob mengira mereka aman, padahal semua pesan dapat disadap dan diubah
4. Dengan kata lain, Diffie-Hellman murni tidak memastikan identitas pihak yang diajak bertukar kunci.

- Pertanyaan 3: Bagaimana cara mencegah serangan MITM pada protokol ini?

Beberapa cara umum:

1. Autentikasi digital
2. Public key ditandatangani menggunakan digital signature (contoh: RSA, ECDSA)
3. Membuktikan bahwa public key benar milik pihak terkait
4. Menggunakan sertifikat digital (PKI)
5. CA (Certificate Authority) menjamin keaslian public key
6. DH dalam protokol terautentikasi
   Misalnya: TLS, IKE (IPsec), SSH
7. DH hanya bagian dari protokol yang sudah ada autentikasinya
   Kesimpulannya: DH + Autentikasi = Aman dari MITM  
   )

---

## 8. Kesimpulan

Berdasarkan percobaan yang telah dilakukan, dapat disimpulkan bahwa protokol Diffie-Hellman mampu menghasilkan sebuah kunci rahasia bersama meskipun proses pertukaran dilakukan melalui saluran komunikasi publik. Keamanan protokol ini bergantung pada kesulitan perhitungan logaritma diskrit, sehingga penyerang yang hanya mengetahui nilai publik tidak dapat memperoleh kunci rahasia dengan mudah.

Namun, percobaan juga menunjukkan bahwa Diffie-Hellman murni rentan terhadap serangan Man-in-the-Middle (MITM) karena tidak memiliki mekanisme autentikasi bawaan. Pada kondisi tersebut, penyerang dapat menyusup di tengah proses pertukaran kunci dan membuat kedua pihak tanpa sadar berbagi kunci dengan penyerang, bukan satu sama lain.

Oleh karena itu, untuk dapat digunakan secara aman di dunia nyata, protokol Diffie-Hellman harus dikombinasikan dengan mekanisme autentikasi, seperti digital signature, sertifikat digital (PKI), atau diintegrasikan dalam protokol aman seperti TLS dan IPsec. Dengan demikian, pertukaran kunci tetap aman meskipun saluran komunikasi bersifat publik.

---

## 9. Daftar Pustaka

(Cantumkan referensi yang digunakan.  
Contoh:

- Katz, J., & Lindell, Y. _Introduction to Modern Cryptography_.
- Stallings, W. _Cryptography and Network Security_. )

---

## 10. Commit Log

(Tuliskan bukti commit Git yang relevan.  
Contoh:

```
commit abc12345
Author: Fajar Saputro <fajarsaputro82@gmail.com>
Date:   2025-09-20

    week7-diffie-hellman: implementasi diffie-hellman dan laporan )
```
