# fastapi-items

# Simple FastAPI Items Service

Proyek ini merupakan implementasi API sederhana menggunakan **FastAPI** dengan database **SQLite**.  
API ini digunakan untuk menampilkan data item yang tersimpan di dalam database melalui beberapa endpoint yang tersedia.

## Daftar Endpoint

| Endpoint | Method | Fungsi | Output |
|----------|--------|--------|--------|
| /items/ | GET | Menampilkan seluruh data item | List[ItemResponse] |
| /items/{item_id} | GET | Menampilkan data item berdasarkan ID | ItemResponse |

## Tujuan Pembuatan

Tugas ini bertujuan untuk mempelajari cara membuat layanan API sederhana menggunakan framework **FastAPI**.  
Dalam proyek ini juga digunakan **SQLAlchemy** sebagai penghubung antara aplikasi Python dan database SQLite.

Selain itu, digunakan **Pydantic** untuk memastikan format data yang dikirim oleh API sesuai dengan struktur yang telah ditentukan.  
Dokumentasi API dapat langsung dilihat melalui **Swagger UI** yang disediakan otomatis oleh FastAPI.

## Struktur Project

fastapi-items/
├── README.md
├── database.py
├── models.py
├── schemas.py
├── main.py
├── items.db
└── Screenshot Swagger UI.png


## Teknologi yang Digunakan

Beberapa teknologi yang digunakan dalam pembuatan proyek ini antara lain:

- **Python** sebagai bahasa pemrograman utama.
- **FastAPI** untuk membuat REST API.
- **Uvicorn** sebagai server untuk menjalankan aplikasi.
- **SQLAlchemy** sebagai ORM untuk pengelolaan database.
- **SQLite** sebagai database yang digunakan dalam proyek ini.
- **Pydantic** untuk validasi dan format data.
- **Git & GitHub** untuk version control dan penyimpanan repository.
- **Swagger UI** untuk dokumentasi dan pengujian endpoint API secara langsung.

## Cara Menjalankan Program

1. Clone repository
git clone https://github.com/Sitinurhalisatahir/fastapi-items.git

2. Masuk ke folder project
cd fastapi-items

3. Install semua library yang dibutuhkan
pip install -r requirements.txt

4. Jalankan aplikasi FastAPI
uvicorn main:app --reload

5. Buka dokumentasi API melalui browser
http://127.0.0.1:8000/docs

## Swagger UI
<img width="949" height="476" alt="Screenshot 2026-03-10 075625" src="https://github.com/user-attachments/assets/8810de0d-7585-476a-95ae-e30e619c63bb" />





