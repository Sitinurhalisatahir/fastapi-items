# models.py

from sqlalchemy import Column, Integer, String  # tipe kolom database
from database import Base  # mengambil Base dari database.py

class Item(Base):  # membuat model tabel Item
    __tablename__ = "items"  # nama tabel di database

    id = Column(Integer, primary_key=True, index=True)  # kolom id sebagai primary key
    name = Column(String)  # kolom untuk nama item
    description = Column(String)  # kolom untuk deskripsi item