from fastapi import FastAPI
import database_model
from database import engine
from routes.product_routes import router as product_router
from authentication.auth_routes import router as auth_router
database_model.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(product_router)
app.include_router(auth_router)        
@app.get('/')
def hello():
    return "Hola Amigo"

