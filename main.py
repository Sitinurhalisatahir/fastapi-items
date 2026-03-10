#main.py

from fastapi import FastAPI, Depends  # framework FastAPI
from sqlalchemy.orm import Session  # session database

import models  # mengimpor model tabel
import schemas  # mengimpor schema validasi
from database import SessionLocal, engine  # koneksi database

models.Base.metadata.create_all(bind=engine)  # membuat tabel di database

app = FastAPI()  # membuat aplikasi FastAPI

def get_db():  # fungsi untuk mengambil koneksi database
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # menutup koneksi setelah selesai

@app.get("/items/", response_model=list[schemas.ItemSchema])  # endpoint untuk semua item
def read_items(db: Session = Depends(get_db)):
    return db.query(models.Item).all()  # mengambil semua data item

@app.get("/items/{item_id}", response_model=schemas.ItemSchema)  # endpoint item berdasarkan id
def read_item(item_id: int, db: Session = Depends(get_db)):
    return db.query(models.Item).filter(models.Item.id == item_id).first()  # mengambil item sesuai id