# Flask Book Management Application

Aplikasi ini adalah manajemen buku sederhana berbasis web yang menggunakan Flask sebagai framework backend. Aplikasi memungkinkan pengguna untuk menambahkan, mengedit, menghapus, dan melihat daftar buku.

## Features
- **Read**: Melihat daftar buku yang tersedia.
- **Create**: Menambahkan buku baru ke daftar.
- **Update**: Mengedit informasi buku yang sudah ada.
- **Delete**: Menghapus buku dari daftar.

## Installation and Running the Application in Docker

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) sudah terinstal di sistem kita.
- (Opsional) [Docker Compose](https://docs.docker.com/compose/) untuk mempermudah pengelolaan beberapa container.

### Steps to Install Docker
1. **Install Docker di Linux**:
   ```bash
   sudo apt update
   sudo apt install docker.io
   sudo systemctl start docker
   sudo systemctl enable docker

# docker-compose.yml
docker-compose.yml digunakan untuk mengonfigurasi dan menjalankan beberapa container Docker sekaligus. Dalam kasus ini, kita hanya memiliki satu container untuk aplikasi web Next.js. Berikut adalah penjelasan untuk setiap bagian dalam docker-compose.yml:

yaml
Copy code
version: '3.9'
services:
  flask-app:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/app

services: Mendefinisikan layanan yang akan dijalankan dalam container. Di sini, kita memiliki satu layanan yang disebut web.

flask-app : Flask-App adalah aplikasi berbasis web yang dibangun menggunakan Flask, sebuah kerangka kerja (framework) mikro untuk pengembangan aplikasi web dengan Python. Flask sangat populer karena ringan, fleksibel, dan mudah digunakan.

Flask memberikan alat dan komponen inti untuk membangun aplikasi web, tetapi tetap memungkinkan pengembang untuk menambahkan fitur sesuai kebutuhan tanpa banyak batasan.

build: .: Menyatakan bahwa Docker akan membangun image dari Dockerfile yang ada di direktori saat ini (.).

ports: Memetakan port dari container ke port lokal Anda. Di sini, port 5000 di dalam container akan dipetakan ke port 5000 di mesin lokal Anda, yang memungkinkan Anda mengakses aplikasi di http://localhost:5000.

volumes : Pada file docker-compose.yml, instruksi volumes digunakan untuk mendefinisikan mount point antara sistem file host (lokal) dan kontaine
