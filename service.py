from fastapi import Depends,HTTPException
from sqlalchemy.orm import Session
from database import session
from database_model import product as dbpr



def add_product(product,db):
    db_product = dbpr(name = product.name,price=product.price,desc = product.desc,id=product.id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_all_product(db):
    return db.query(dbpr).all()

def get_product_by_id(id,db):
    return db.query(dbpr).filter(dbpr.id == id).first()

def update_product(id,product,db):
    data=db.query(dbpr).filter(dbpr.id == id).first()
    if data is None:
        raise HTTPException(status_code=404,detail="Product not found")
    data.name = product.name
    data.price = product.price
    data.desc = product.desc
    db.commit()
    db.refresh(data)
    return data

def delete_product(id,db):
    data = db.query(dbpr).filter(dbpr.id == id).first()
    if data is None:
        raise HTTPException(status_code=404,detail="Product not found")
    db.delete(data)
    db.commit()
    return {"msg":"Product deleted succesfully"}