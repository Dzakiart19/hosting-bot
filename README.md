# Panel Kontrol Bot Telegram

Ini adalah proyek panel web sederhana untuk mengontrol Bot Telegram. Anda dapat mengirim pesan ke pengguna, grup, atau channel langsung dari antarmuka web.

## Teknologi yang Digunakan

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Telegram API**: `python-telegram-bot`

## Struktur Proyek

```
.
├── backend/
│   └── app.py        # Logika server Flask dan bot
├── frontend/
│   ├── index.html    # Halaman utama panel
│   ├── style.css     # Styling untuk panel
│   └── script.js     # Logika sisi klien
├── requirements.txt  # Dependensi Python
└── README.md         # File ini
```

## Cara Menjalankan Proyek

### 1. Prasyarat

- Python 3.6+
- `pip` untuk menginstal dependensi Python
- Token Bot Telegram. Anda bisa mendapatkannya dari [@BotFather](https://t.me/BotFather).

### 2. Instalasi

1.  **Clone repositori ini (atau unduh file-filenya).**

2.  **Instal dependensi Python:**
    ```bash
    pip install -r requirements.txt
    ```

### 3. Konfigurasi

1.  **Buka file `backend/app.py`.**
2.  Cari baris berikut:
    ```python
    BOT_TOKEN = os.environ.get('BOT_TOKEN', 'GANTI_DENGAN_TOKEN_BOT_ANDA')
    ```
3.  Ganti `'GANTI_DENGAN_TOKEN_BOT_ANDA'` dengan token bot Anda yang sebenarnya.

    **Penting:** Untuk keamanan, sangat disarankan menggunakan variabel lingkungan (`environment variables`) untuk menyimpan token Anda daripada menuliskannya langsung di kode, terutama jika Anda akan men-deploy-nya.

### 4. Menjalankan Server Backend

1.  Buka terminal atau command prompt.
2.  Arahkan ke direktori root proyek.
3.  Jalankan server Flask:
    ```bash
    python backend/app.py
    ```
4.  Server akan berjalan di `http://127.0.0.1:5000`.

### 5. Menggunakan Panel Web

1.  Pastikan server backend Anda sedang berjalan (langkah 4).
2.  Buka browser web Anda.
3.  Akses alamat berikut:
    ```
    http://127.0.0.1:5000/
    ```
4.  Panel kontrol web sekarang akan muncul, siap digunakan. Anda dapat memasukkan Chat ID dan pesan untuk dikirim melalui bot Anda.

## Cara Menjalankan dengan Docker (Opsional)

Jika Anda memiliki Docker terinstal, Anda dapat membangun dan menjalankan aplikasi ini sebagai container.

1.  **Bangun (Build) Docker Image:**
    Dari direktori root proyek, jalankan perintah berikut. Jangan lupa untuk mengganti `nama-panel-anda` dengan nama yang Anda inginkan untuk image tersebut.
    ```bash
    docker build -t nama-panel-anda .
    ```

2.  **Jalankan Docker Container:**
    Setelah image berhasil dibangun, jalankan sebagai container. Anda perlu meneruskan `BOT_TOKEN` Anda sebagai variabel lingkungan.
    ```bash
    docker run -p 5000:5000 -e BOT_TOKEN="TOKEN_BOT_ANDA_DI_SINI" nama-panel-anda
    ```
    - `-p 5000:5000`: Memetakan port 5000 di mesin Anda ke port 5000 di dalam container.
    - `-e BOT_TOKEN="..."`: Mengatur variabel lingkungan `BOT_TOKEN` di dalam container. Ganti `TOKEN_BOT_ANDA_DI_SINI` dengan token Anda.

3.  **Akses Panel:**
    Buka browser Anda dan akses `http://localhost:5000`.