# Gunakan base image Python yang resmi
FROM python:3.9-slim

# Tetapkan direktori kerja di dalam container
WORKDIR /app

# Salin file requirements.txt terlebih dahulu untuk memanfaatkan caching layer Docker
COPY requirements.txt .

# Instal dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode aplikasi (backend dan frontend) ke dalam direktori kerja
COPY ./backend /app/backend
COPY ./frontend /app/frontend

# Ekspos port yang digunakan oleh aplikasi Flask
EXPOSE 5000

# Perintah untuk menjalankan aplikasi saat container dijalankan
# Gunakan gunicorn untuk production atau server development Flask untuk pengujian
# Di sini kita akan menggunakan server development Flask untuk kesederhanaan.
# Untuk production, ganti dengan: CMD ["gunicorn", "--bind", "0.0.0.0:5000", "backend.app:app"]
CMD ["python", "backend/app.py"]
