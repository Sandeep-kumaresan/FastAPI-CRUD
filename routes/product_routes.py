from fastapi import APIRouter,Depends
import services.product_service as service
from models import Product
from database import session,db_conn
from authentication.auth import get_current_user
from sqlalchemy.orm import Session

router = APIRouter(prefix="/products")
@router.post('/add')
def add_products(product: Product,db:Session = Depends(db_conn), user_id=Depends(get_current_user)):
    return service.add_product(product,db)
    
@router.get('/getall')
def get_all_products(db:Session = Depends(db_conn),user_id=Depends(get_current_user)):
    return service.get_all_product(db)

@router.get('/get/{id}')
def get_by_id(id:int,db:Session = Depends(db_conn),user_id=Depends(get_current_user)):
    return service.get_product_by_id(id,db)

@router.put('/edit/{id}')
def update_products(id: int,product:Product,db:Session = Depends(db_conn),user_id=Depends(get_current_user)):
    return service.update_product(id,product,db)

@router.delete('/delete/{id}')
def delete_products(id,db:Session = Depends(db_conn),user_id=Depends(get_current_user)):
    return service.delete_product(id,db)