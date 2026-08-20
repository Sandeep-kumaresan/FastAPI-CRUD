from sqlalchemy.orm import declarative_base,relationship
from sqlalchemy import Integer,Column,String,Float,ForeignKey
Base = declarative_base()
class Product(Base):
    __tablename__ = "product"
    id = Column(Integer,primary_key=True)
    name=Column(String)
    price=Column(Float)
    desc=Column(String)
    order=relationship("User_order",back_populates="product")

class User(Base):
    __tablename__ ="user"
    email = Column(String,primary_key=True)
    password = Column(String,nullable=False)
    order=relationship("User_order",back_populates="user")
    
class User_order(Base):
    __tablename__="userorder"
    id=Column(Integer,primary_key=True)
    email_id=Column(String,ForeignKey(User.email))
    product_id=Column(Integer,ForeignKey(Product.id))
    product = relationship("Product",back_populates="order")
    user=relationship("User",back_populates="order")