# Eraspace Get Cookies
Skrip Python untuk melakukan auto login ke akun Eraspace dan menyimpan token (cookies) secara otomatis ke dalam file cookies/cookies.json.
Mendukung multiple akun melalui input dari file CSV.

## Fitur Utama
 - Auto login ke akun Eraspace
 - Input password untuk setiap nomor secara manual
 - Menyimpan token ke ```cookies.json```
 - Memperbarui token jika nomor sudah tersimpan
 - Membaca daftar akun dari ```akun/akun.csv```
 - Menggunakan HTTPX untuk request cepat & stabil

## Struktur Folder
```
Eraspace-Get-Cookies/
│
├── akun/
│   └── akun.csv
│
├── cookies/
│   └── cookies.json   (otomatis dibuat)
│
├── main.py
├── requirements.txt
└── README.md
```

## Persyaratan
Pastikan Anda sudah menginstal Python 3.8+

## Install Dependencies
Jalankan perintah berikut:
   ```pip install -r requirements.txt```

## Cara Menggunakan
### 1. Siapkan File ```akun/akun.csv```
Format isi file :
```
08xxxxxxxxxx
08xxxxxxxxxx
08xxxxxxxxxx
...
```

### 2. Jalankan Script
```
python main.py
```

### 3. Masukkan Password
Untuk setiap nomor di CSV, program akan meminta password:
```
Memproses nomor: 08xxxxxxxxxx
Masukkan password untuk 08xxxxxxxxxx:
```

### 4. Token Tersimpan
Jika login berhasil, token akan disimpan ke:
```
cookies/cookies.json
```
Format penyimpanan:
```
[
    {
        "nomor": "08xxxxxxxxxx",
        "cookies": "TOKEN_HERE"
    }
]
```
Jika nomor sudah ada, token akan diperbarui otomatis.

# Kode Utama
Kode lengkap dapat dilihat di ```main.py```
(Sudah termasuk login, pembacaan CSV, dan penyimpanan token)

# Support
Jika Anda ingin update fitur, perbaikan bug, atau custom tools, silakan buat Issue atau Pull Request.

# Berikan Star di GitHub
Jika script ini bermanfaat, dukung dengan memberikan ⭐ pada repository! :)
