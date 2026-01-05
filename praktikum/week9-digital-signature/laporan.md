# Laporan Praktikum Kriptografi

Minggu ke-: X  
Topik: [Digital Signature]  
Nama: [Fajar Saputro]  
NIM: [230202749]  
Kelas: [5IKRB]

---

## 1. Tujuan

(Tuliskan tujuan pembelajaran praktikum sesuai modul.)
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1. Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.
2. Memverifikasi keaslian tanda tangan digital.
3. Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.

---

## 2. Dasar Teori

Tanda tangan digital (digital signature) merupakan mekanisme kriptografi yang digunakan untuk menjamin keaslian dan integritas suatu pesan atau dokumen digital. Berbeda dengan tanda tangan konvensional, tanda tangan digital memanfaatkan algoritma kriptografi kunci publik sehingga hanya pemilik kunci privat yang dapat menghasilkan tanda tangan yang sah.

Algoritma RSA adalah salah satu algoritma kriptografi kunci publik yang umum digunakan dalam implementasi tanda tangan digital. Pada proses penandatanganan, pesan terlebih dahulu di-hash menggunakan fungsi hash kriptografis (misalnya SHA-256), kemudian hasil hash tersebut dienkripsi menggunakan kunci privat pengirim. Hasil enkripsi inilah yang disebut sebagai tanda tangan digital.

## Proses verifikasi dilakukan dengan cara mendekripsi tanda tangan menggunakan kunci publik pengirim, kemudian membandingkan hasilnya dengan hash pesan yang diterima. Jika kedua nilai tersebut sama, maka pesan dipastikan tidak mengalami perubahan dan benar berasal dari pengirim yang sah.

## 3. Alat dan Bahan

(- Python 3.x

- Visual Studio Code / editor lain
- Git dan akun GitHub
- Library tambahan (misalnya pycryptodome, jika diperlukan) )

---

## 4. Langkah Percobaan

(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
Membuat struktur folder:

praktikum/week9-digital-signature/
├─ src/
├─ screenshots/
└─ laporan.md

Menginstal library kriptografi dengan perintah:

pip install pycryptodome

Membuat file src/signature.py.

Mengimplementasikan:

Generate pasangan kunci RSA

Pembuatan tanda tangan digital

Verifikasi tanda tangan

Uji verifikasi gagal pada pesan yang dimodifikasi

1. Menjalankan program:
   python signature.py
   2.Mengambil screenshot hasil eksekusi dan menyimpannya di folder screenshots/.

---

## 5. Source Code

(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate pasangan kunci RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Pesan yang akan ditandatangani
message = b"Hello, ini pesan penting."
h = SHA256.new(message)

# Buat tanda tangan dengan private key
signature = pkcs1_15.new(private_key).sign(h)
print("Signature:", signature.hex())
try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Verifikasi berhasil: tanda tangan valid.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid.")
# Modifikasi pesan
fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)
try:
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("Verifikasi berhasil (seharusnya gagal).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")...
```

)

---

## 6. Hasil dan Pembahasan

(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).

- Berikan tabel atau ringkasan hasil uji jika diperlukan.
- Jelaskan apakah hasil sesuai ekspektasi.
- Bahas error (jika ada) dan solusinya.

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/image.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan

(Jawab pertanyaan diskusi yang diberikan pada modul.

- Pertanyaan 1: …
- Pertanyaan 2: …  
  )

---

## 8. Kesimpulan

(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan. )

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

    week9-cryptosystem: digital-signature )
```
