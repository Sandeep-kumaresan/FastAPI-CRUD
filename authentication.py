from jose import jwt
from datetime import datetime,timedelta
import os
def create_jwt(email: str):
    SECRET_KEY=os.getenv("SECRET_KEY")
    ALGORITHM=os.getenv("ALGORITHM")
    payload={
        "sub":str(email),
        "exp":datetime.utcnow()+timedelta(minutes=180)
    }
    token = jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    return token