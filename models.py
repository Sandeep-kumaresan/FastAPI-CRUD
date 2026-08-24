from pydantic import BaseModel,EmailStr

class Product(BaseModel):
    id:int
    name:str
    price:float
    desc:str
class User(BaseModel):
    email:EmailStr
    password:str
