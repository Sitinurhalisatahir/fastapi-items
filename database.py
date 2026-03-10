# database.py

from sqlalchemy import create_engine  # untuk membuat koneksi ke database
from sqlalchemy.orm import sessionmaker, declarative_base  # untuk membuat session dan base model

DATABASE_URL = "sqlite:///./items.db"  # alamat database SQLite

engine = create_engine(  # membuat koneksi aplikasi ke database
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)  # membuat session untuk akses database

Base = declarative_base()  # class dasar untuk membuat tabel model