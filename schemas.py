from pydantic import BaseModel

class ItemSchema(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True