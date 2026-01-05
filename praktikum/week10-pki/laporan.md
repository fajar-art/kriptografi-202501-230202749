D# Laporan Praktikum Kriptografi
Minggu ke-: 10  
Topik: [PKI]  
Nama: [Fajar Saputro]  
NIM: [230202749]  
Kelas: [5IKRB]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Membuat sertifikat digital sederhana.  
2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.  
3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).  

---

## 2. Dasar Teori
Public Key Infrastructure (PKI) merupakan suatu sistem yang digunakan untuk mengelola kunci publik dan sertifikat digital dengan tujuan menjamin keamanan komunikasi serta keaslian identitas dalam sistem informasi. PKI memanfaatkan kriptografi kunci publik (asymmetric cryptography) yang menggunakan sepasang kunci, yaitu kunci privat (private key) yang bersifat rahasia dan kunci publik (public key) yang dapat dibagikan kepada pihak lain. Melalui mekanisme ini, PKI mampu menyediakan layanan keamanan seperti autentikasi, integritas data, kerahasiaan informasi, serta non-repudiation atau jaminan bahwa suatu pihak tidak dapat menyangkal tindakan yang telah dilakukannya.

Sertifikat digital merupakan komponen utama dalam PKI yang berfungsi sebagai bukti elektronik untuk mengaitkan identitas suatu entitas dengan kunci publiknya. Sertifikat digital umumnya mengikuti standar X.509 yang berisi informasi penting seperti identitas pemilik sertifikat (subject), identitas penerbit sertifikat (issuer), kunci publik, nomor seri sertifikat, masa berlaku, serta tanda tangan digital dari pihak penerbit. Tanda tangan digital ini memastikan bahwa sertifikat tidak mengalami perubahan dan benar-benar diterbitkan oleh pihak yang berwenang.

Dalam sistem PKI, pihak yang berperan sebagai penerbit sertifikat disebut Certificate Authority (CA). CA bertugas untuk memverifikasi identitas pemohon sertifikat dan menandatangani sertifikat tersebut menggunakan kunci privat miliknya. Pada implementasi tertentu, seperti pada kegiatan pembelajaran atau pengujian, sertifikat dapat bersifat self-signed, yaitu sertifikat yang ditandatangani oleh pemiliknya sendiri. Pada jenis sertifikat ini, nilai subject dan issuer memiliki identitas yang sama sehingga tidak melibatkan CA eksternal.
---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (cryptography)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `pki.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python pki.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

# Generate key pair
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Buat subject & issuer (CA sederhana = self-signed)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
])

# Buat sertifikat
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))
    .sign(key, hashes.SHA256())
)

# Simpan sertifikat
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Sertifikat digital berhasil dibuat: cert.pem")


---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Hasil   
- Jelaskan apakah hasil sesuai ekspektasi.  
- tidak ada error

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshoots/image.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Bagaimana browser memverifikasi sertifikat HTTPS?:
Saat pengguna membuka sebuah website menggunakan HTTPS, browser akan menerima sertifikat digital dari server. Browser kemudian mengecek apakah sertifikat tersebut dikeluarkan oleh Certificate Authority (CA) yang terpercaya dan sudah terdaftar di dalam sistem atau browser. Selain itu, browser juga memeriksa masa berlaku sertifikat, kecocokan nama domain pada sertifikat dengan alamat website yang diakses, serta keabsahan tanda tangan digitalnya. Jika semua pengecekan tersebut berhasil, browser akan menganggap koneksi aman dan komunikasi bisa dilanjutkan dengan enkripsi.  
- Apa yang terjadi jika CA palsu menerbitkan sertifikat?:
Jika CA palsu atau tidak terpercaya menerbitkan sertifikat digital, biasanya browser akan langsung memberikan peringatan keamanan kepada pengguna karena sertifikat tersebut tidak memiliki rantai kepercayaan yang valid. Namun, jika CA palsu berhasil dipercaya oleh sistem, hal ini bisa sangat berbahaya. Penyerang dapat menyamar sebagai website asli dan melakukan serangan man-in-the-middle, sehingga data penting seperti username, password, atau informasi transaksi berisiko dicuri tanpa diketahui oleh pengguna.
)
- Mengapa PKI penting dalam komunikasi aman (misalnya transaksi online)?:
PKI sangat penting dalam komunikasi aman karena berfungsi sebagai dasar kepercayaan dalam pertukaran data di internet. Dalam transaksi online seperti belanja daring atau internet banking, PKI memastikan bahwa pengguna terhubung ke server yang benar dan bukan ke pihak palsu. Selain itu, PKI juga melindungi data yang dikirim agar tidak bisa dibaca atau diubah oleh pihak lain. Dengan adanya PKI, komunikasi dan transaksi digital dapat dilakukan dengan lebih aman dan terpercaya.
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

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
