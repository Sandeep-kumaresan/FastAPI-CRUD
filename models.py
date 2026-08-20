from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    price:float
    desc:str
class User(BaseModel):
    email:str
    password:str
