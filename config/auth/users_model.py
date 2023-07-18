from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str 

class User(BaseModel):
    Username: str
    Email: str 
    Full_Name: str 
    Disabled: int 
