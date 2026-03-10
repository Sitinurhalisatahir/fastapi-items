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

## Struktur Folder
