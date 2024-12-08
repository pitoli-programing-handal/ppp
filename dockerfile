# Gunakan image Python sebagai base image
FROM python:3.9-slim

# Tetapkan direktori kerja
WORKDIR /app

# Salin requirements.txt (daftar pustaka Python yang diperlukan)
COPY requirements.txt requirements.txt

# Install pustaka Python
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file aplikasi ke container
COPY . .

# Tetapkan port Flask
EXPOSE 5000

# Perintah untuk menjalankan aplikasi
CMD ["python", "app.py"]
