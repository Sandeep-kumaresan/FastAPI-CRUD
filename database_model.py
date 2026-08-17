from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer,Column,String,Float
Base = declarative_base()
class product(Base):
    __tablename__ = "product"
    id = Column(Integer,primary_key=True)
    name=Column(String)
    price=Column(Float)
    desc=Column(String)

class user(Base):
    __tablename__ ="user"
    id = Column(Integer,primary_key=True)
    email = Column(String,nullable=False)
    password = Column(String,nullable=False)