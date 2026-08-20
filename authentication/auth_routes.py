from fastapi import APIRouter,Depends
from database import db_conn
from authentication import auth
from models import User
router = APIRouter(prefix="/auth")

@router.post("/login")
def login(user: User,db = Depends(db_conn)):
    return auth.login(user,db)

@router.post("/signup")
def signup(user : User, db=Depends(db_conn)):
    return auth.signup(user,db)