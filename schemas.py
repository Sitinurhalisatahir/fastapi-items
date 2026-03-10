# schemas.py

from pydantic import BaseModel  # untuk membuat schema validasi data

class ItemSchema(BaseModel):  # schema untuk output API
    id: int  # id bertipe integer
    name: str  # nama item bertipe string
    description: str  # deskripsi item bertipe string

    class Config:
        from_attributes = True  # menghubungkan schema dengan model ORM