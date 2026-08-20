from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException
from datetime import datetime,timedelta
from database_model import User
from pwdlib import PasswordHash
import os

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")
oauth2 = OAuth2PasswordBearer(tokenUrl="login")
password_hash=PasswordHash.recommended()
def create_jwt(email: str):
    
    payload={
        "sub":str(email),
        "exp":datetime.utcnow()+timedelta(minutes=180)
    }
    token = jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    return token

def get_current_user(token:str = Depends (oauth2)):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        useremail = payload.get("sub")
        if useremail is None:
            raise HTTPException(status_code=401,detail="Invalid token")
        return useremail
    except JWTError:
        raise HTTPException(status_code=401,detail="Invalid or expired token")
    
def login(user,db):
    log = db.query(User).filter(User.email==user.email).first()
    valid = password_hash.verify(user.password,log.password)
    token = create_jwt(user.email)
    if valid:
        return token
    else:
        return "Invalid Login"

def signup(user,db):
    hashed_pass = password_hash.hash(user.password)
    print(hashed_pass)
    usermodel = User(email=user.email,password=hashed_pass)
    db.add(usermodel)
    db.commit()
    db.refresh(usermodel)
    return "Signup success, Try login"