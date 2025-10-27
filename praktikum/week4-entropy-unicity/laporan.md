# Laporan Praktikum Kriptografi

Minggu ke-: 4  
Topik: [Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)]  
Nama: [Fajar Saputro]  
NIM: [230202749]  
Kelas: [5IKRB]

---

## 1. Tujuan

Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

1. Menyelesaikan perhitungan sederhana terkait entropi kunci.
2. Menggunakan teorema Euler pada contoh perhitungan modular & invers.
3. Menghitung **unicity distance** untuk ciphertext tertentu.
4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.

---

## 2. Dasar Teori

Entropy dan unicity distance digunakan untuk mengevaluasi kekuatan suatu kunci dalam sistem kriptografi. Entropy menggambarkan tingkat keacakan kunci—semakin tinggi nilai entropinya, semakin sulit kunci ditebak oleh penyerang. Nilai ini biasanya dinyatakan dalam bit dan menunjukkan seberapa besar ruang kemungkinan kunci yang ada. Kunci dengan entropi rendah mudah diprediksi, sehingga berisiko terhadap serangan brute force.

Unicity distance menunjukkan jumlah minimum ciphertext yang dibutuhkan agar kunci dapat ditentukan secara unik secara teoritis. Jika panjang ciphertext masih di bawah nilai ini, cipher dianggap aman karena banyak kemungkinan kunci masih dapat menghasilkan plaintext yang tampak masuk akal. Dalam cipher klasik seperti Vigenère atau Caesar, unicity distance cenderung rendah karena pola bahasa mudah dikenali.

Kedua konsep ini penting untuk menilai ketahanan cipher terhadap brute force attack, yaitu percobaan semua kemungkinan kunci. Meski algoritma modern seperti AES sangat kuat, serangan brute force tetap relevan bila entropi kunci rendah atau implementasi tidak benar. Dengan demikian, kunci acak dengan entropi tinggi dan panjang ciphertext yang memadai menjadi dasar utama keamanan kriptografi.

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
def encrypt(text, key):
    return ...
```

)

---

## 6. Hasil dan Pembahasan

(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).

- Berikan tabel atau ringkasan hasil uji jika diperlukan.
- Jelaskan apakah hasil sesuai ekspektasi.
- Bahas error (jika ada) dan solusinya.

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](Hasil_Running_bruteforche.png)
)

---

## 7. Jawaban Pertanyaan

(Jawab pertanyaan diskusi yang diberikan pada modul.

- Pertanyaan 1: Entropy (Kekuatan Kunci)
  Mengukur tingkat keacakan kunci.
  Semakin tinggi entropi → semakin sulit ditebak → kunci makin kuat.
- Pertanyaan 2: Unicity Distance
  Jumlah minimum ciphertext agar kunci bisa ditentukan secara unik.
  Jika ciphertext < unicity distance → cipher masih aman.
- Pertanyaan 3: Brute Force Masih Ancaman
  Karena kunci sering lemah, manusia ceroboh, dan teknologi makin cepat — meski algoritma kuat.
  )

---

## 8. Kesimpulan

Berdasarkan percobaan, semakin tinggi nilai entropi, semakin kuat kunci terhadap serangan brute force karena ruang kemungkinan kunci makin besar. Nilai unicity distance menunjukkan batas keamanan teoritis cipher; jika ciphertext lebih pendek dari nilai ini, kunci masih sulit ditebak. Dengan demikian, kunci acak dan panjang sangat penting untuk menjaga keamanan sistem kriptografi.

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
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
