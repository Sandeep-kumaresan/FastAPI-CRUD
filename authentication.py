from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException
from datetime import datetime,timedelta
import os

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

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