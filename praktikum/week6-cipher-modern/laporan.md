# Laporan Praktikum Kriptografi

Minggu ke-: X  
Topik: [judul praktikum]  
Nama: [Fajar Saputro]  
NIM: [230202749]  
Kelas: [5IKRB]

---

## 1. Tujuan

(
    1. Mengimplementasikan algoritma DES untuk blok data sederhana.
    2. Menerapkan algoritma AES dengan panjang kunci 128 bit.3. Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.)

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
#Implementasi DES
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)  # kunci 64 bit (8 byte)
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b"ABCDEFGH"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)


#implementasi AES-128
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # 128 bit key
cipher = AES.new(key, AES.MODE_EAX)

plaintext = b"Modern Cipher AES Example"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

print("Ciphertext:", ciphertext)

# Dekripsi
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher_dec.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())


#implementasi RSA
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Enkripsi dengan public key
cipher_rsa = PKCS1_OAEP.new(public_key)
plaintext = b"RSA Example"
ciphertext = cipher_rsa.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Dekripsi dengan private key
decipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = decipher_rsa.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
...
```

)

---

## 6. Hasil dan Pembahasan

(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).

- hasil ujinya sesuai dengan ekspektasi dan mendecrypt serta mengencrypt sesuai dengan modul.
- hasil sesuai ekspektasi.
- terdapat error dimana library yang dipanggil belum ada di perangkat. sehingga harus mendownload dulu.

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi DES](screenshots/DES.png)
![Hasil Eksekusi AES-128](screenshots/AES.png)
![Hasil Eksekusi RSA](screenshots/RSA.png)
)

---

## 7. Jawaban Pertanyaan

(Jawab pertanyaan diskusi yang diberikan pada modul.

- Pertanyaan 1: Perbedaan mendasar antara DES, AES, dan RSA dalam hal kunci dan keamanan

DES (Data Encryption Standard)
Menggunakan kunci simetris, panjang kunci hanya 56-bit. Karena kunci terlalu pendek, DES dapat di-brute force dengan cepat di era komputasi modern. Keamanannya saat ini dianggap tidak lagi memadai.

AES (Advanced Encryption Standard)
Juga merupakan cipher simetris, tetapi memiliki panjang kunci jauh lebih kuat yaitu 128, 192, atau 256-bit. AES aman terhadap brute-force dan menjadi standar enkripsi modern yang digunakan secara luas.

RSA (Rivest–Shamir–Adleman)
Menggunakan kunci asimetris (public key dan private key berbeda). Keamanan RSA didasarkan pada kesulitan memfaktorkan bilangan prima besar, sehingga kunci biasanya 2048–4096 bit, jauh lebih panjang dari kunci AES.

Kesimpulannya:
DES dan AES adalah simetris, RSA adalah asimetris. AES jauh lebih aman dibanding DES, dan RSA digunakan untuk pertukaran kunci dan tanda tangan digital, bukan untuk enkripsi data dalam jumlah besar karena lebih lambat.
- Pertanyaan 2: …Mengapa AES lebih banyak digunakan dibanding DES di era modern?
Kunci DES hanya 56-bit → rentan brute-force.

AES memiliki struktur dan ukuran kunci yang jauh lebih kuat (128/192/256-bit).

AES lebih efisien di perangkat modern, dapat dipercepat oleh hardware.

AES telah menjadi standar internasional (NIST) dan sudah terbukti tahan terhadap berbagai jenis serangan kriptografi modern.

Intinya: DES sudah tidak aman, AES sangat aman dan cepat, sehingga AES menjadi pilihan utama saat ini. 
- Pertanyaan 3: Mengapa RSA dikategorikan sebagai algoritma asimetris dan bagaimana proses pembangkitan kuncinya?

RSA dikategorikan asimetris karena menggunakan pasangan kunci berbeda:

Public key → digunakan untuk enkripsi (boleh diketahui umum)

Private key → digunakan untuk dekripsi (dirahasiakan)

RSA bergantung pada matematika bilangan prima besar dan masalah faktorisasi yang sulit.

Proses pembangkitan kunci RSA secara sederhana:

Pilih dua bilangan prima besar p dan q

Hitung n = p × q (modulus)

Hitung φ(n) = (p − 1)(q − 1)

Pilih bilangan e yang relatif prima dengan φ(n) → public exponent

Hitung d sebagai invers modulo:
d × e ≡ 1 (mod φ(n))

Hasil:

Public key = (e, n)

Private key = (d, n)  
  )

---

## 8. Kesimpulan

Pada praktikum ini telah berhasil dilakukan implementasi tiga algoritma kriptografi modern yaitu DES, AES, dan RSA. Melalui percobaan pada blok data sederhana, algoritma DES dapat mengenkripsi dan mendekripsi data dengan benar, namun percobaan juga menunjukkan bahwa DES memiliki panjang kunci yang terlalu pendek sehingga keamanannya sudah tidak lagi memadai untuk digunakan di era sekarang.

Implementasi AES dengan kunci 128-bit terbukti berjalan lebih baik dan lebih aman, sekaligus menunjukkan efisiensi serta kekuatan enkripsi yang menjadikannya standar utama dalam kriptografi modern untuk melindungi data secara simetris. Sementara itu, implementasi algoritma RSA memberi gambaran bagaimana konsep kunci publik dan privat bekerja untuk keamanan asimetris, khususnya dalam proses enkripsi, dekripsi, dan pertukaran kunci secara aman.

Dari keseluruhan percobaan, dapat disimpulkan bahwa kriptografi modern mengutamakan keamanan berbasis panjang kunci yang kuat dan struktur algoritma yang tahan terhadap serangan brute-force maupun analisis kriptografi lainnya. Dengan demikian, AES dan RSA menjadi pilihan utama dalam berbagai sistem keamanan informasi terkini, sedangkan DES sudah tidak direkomendasikan lagi karena kelemahannya yang mudah dieksploitasi.
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
Author: Fajarsaputro82@gmail.com <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
