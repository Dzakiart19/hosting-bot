# Panduan Pengguna Panel Hosting Bot

Selamat datang di Panel Hosting Bot! Platform ini memungkinkan Anda untuk mendeploy aplikasi Anda dengan mudah langsung dari file `.zip`.

## 1. Registrasi Akun

Semua interaksi dimulai melalui bot Telegram kami.

1.  **Mulai Bot:** Buka Telegram dan cari bot resmi kami (admin akan memberikan nama botnya). Tekan tombol **"Start"**.
2.  **Registrasi:** Bot akan membalas dengan tombol **"Register"**. Tekan tombol ini.
3.  **Otorisasi:** Telegram akan meminta izin Anda untuk membagikan informasi dasar profil Anda dengan kami untuk membuat akun. Setujui permintaan ini.
4.  **Selesai!** Setelah berhasil, Anda akan menerima pesan konfirmasi dan tautan unik untuk mengakses dashboard web Anda. Tautan ini sudah termasuk token login, jadi Anda tidak perlu kata sandi.

*(Contoh screenshot alur registrasi akan ditambahkan di sini)*

## 2. Upload Proyek Anda

1.  **Akses Dashboard:** Buka tautan dashboard yang diberikan oleh bot.
2.  **Upload File .zip:** Klik tombol **"Upload Project"**. Pilih file `.zip` dari proyek Anda (maksimal 100 MB).
3.  **Proses Deploy:** Setelah diunggah, sistem kami akan secara otomatis:
    *   Memindai file dari virus.
    *   Mendeteksi bahasa pemrograman (runtime) yang Anda gunakan.
    *   Membangun proyek Anda menjadi sebuah container Docker.
    *   Mendeploy container tersebut ke subdomain unik, contoh: `<uuid>.panelhost.my.id`.
4.  **Notifikasi:** Anda akan menerima notifikasi di Telegram setelah proyek Anda berhasil di-deploy, lengkap dengan tautannya.

## 3. Struktur Proyek yang Didukung

Agar proses deteksi otomatis berhasil, pastikan struktur proyek Anda mengikuti panduan ini.

### Python (Flask/FastAPI)

-   Harus ada file `requirements.txt` di root direktori.
-   File utama Anda harus bernama `main.py`.
-   Aplikasi Anda harus berjalan di port `8000`. Port ini secara otomatis disediakan melalui environment variable `PORT`.

**Contoh `main.py` (Flask):**
```python
import os
from flask import Flask

app = Flask(__name__)
port = int(os.environ.get("PORT", 8000))

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
```

### Node.js

-   Harus ada file `package.json` di root direktori.
-   File utama Anda harus `index.js` (atau didefinisikan di `package.json` -> `main`).
-   Aplikasi Anda harus berjalan di port `3000`. Gunakan `process.env.PORT`.

**Contoh `index.js` (Express):**
```javascript
const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
```

### PHP

-   Harus ada file `index.php` di root direktori.
-   Server web (Nginx) secara otomatis dikonfigurasi untuk menjalankan file PHP di port `80`.

## 4. Environment Variables

Sistem secara otomatis menyuntikkan environment variable `PORT` ke dalam container Anda. Anda harus menggunakan variabel ini untuk menjalankan server aplikasi Anda. Variabel lain dapat dikonfigurasi melalui dashboard web di masa mendatang.

## 5. Menggunakan Dockerfile Kustom

Jika proyek Anda memerlukan langkah-langkah build yang lebih kompleks, Anda dapat menyertakan `Dockerfile` Anda sendiri di dalam file `.zip`. Jika sistem kami mendeteksi `Dockerfile`, maka file tersebut akan digunakan untuk membangun proyek Anda, bukan proses deteksi otomatis.

## 6. Perintah Bot

Anda dapat mengelola proyek Anda langsung dari Telegram menggunakan perintah berikut:

-   `/list`: Menampilkan semua proyek Anda yang aktif beserta statusnya.
-   `/stop <uuid>`: Menghentikan container proyek tertentu.
-   `/start <uuid>`: Menjalankan kembali container proyek yang dihentikan.
-   `/delete <uuid>`: Menghentikan dan menghapus proyek secara permanen.
-   `/logs <uuid>`: Menampilkan log terbaru dari container proyek Anda.
