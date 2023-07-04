from pydantic import BaseModel
from datetime import datetime

class PunDisplay(BaseModel):
    Title: str
    Question: str
    Answer: str

    class Config:
        orm_mode = True
class PunCreate(BaseModel):
    Title: str
    Question: str
    Answer: str
    
    class Config:
        orm_mode = True
 