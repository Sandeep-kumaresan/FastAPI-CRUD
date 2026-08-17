from fastapi import Depends, FastAPI
import database_model
from sqlalchemy.orm import Session
from models import Product
from database import engine
from database import session
import service
database_model.Base.metadata.create_all(bind=engine)
app = FastAPI()
def db_conn():
    db=session()
    try:
        yield db
    finally:
        db.close()
        
@app.get('/')
def hello():
    return "Hola Amigo"

@app.post('/add')
def add_products(product: Product,db:Session = Depends(db_conn) ):
    return service.add_product(product,db)
    
@app.get('/getall')
def get_all_products(db:Session = Depends(db_conn)):
    return service.get_all_product(db)

@app.get('/get/{id}')
def get_by_id(id:int,db:Session = Depends(db_conn)):
    return service.get_product_by_id(id,db)

@app.put('/edit/{id}')
def update_products(id: int,product:Product,db:Session = Depends(db_conn)):
    return service.update_product(id,product,db)

@app.delete('/delete/{id}')
def delete_products(id,db:Session = Depends(db_conn)):
    return service.delete_product(id,db)