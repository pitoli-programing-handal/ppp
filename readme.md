# Flask Book Management Application

Aplikasi ini adalah manajemen buku sederhana berbasis web yang menggunakan Flask sebagai framework backend. Aplikasi memungkinkan pengguna untuk menambahkan, mengedit, menghapus, dan melihat daftar buku.

## Features
- **Read**: Melihat daftar buku yang tersedia.
- **Create**: Menambahkan buku baru ke daftar.
- **Update**: Mengedit informasi buku yang sudah ada.
- **Delete**: Menghapus buku dari daftar.

## Installation and Running the Application in Docker

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) sudah terinstal di sistem Anda.
- (Opsional) [Docker Compose](https://docs.docker.com/compose/) untuk mempermudah pengelolaan beberapa container.

### Steps to Install Docker
1. **Install Docker di Linux**:
   ```bash
   sudo apt update
   sudo apt install docker.io
   sudo systemctl start docker
   sudo systemctl enable docker
