from fastapi import FastAPI
import os
import database_model
from database import engine
from google import genai
from routes.product_routes import router as product_router
from authentication.auth_routes import router as auth_router
database_model.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(product_router)
app.include_router(auth_router) 
API_KEY=os.getenv("API_KEY")        
client = genai.Client(api_key=API_KEY)
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Explain JWT authentication in simple terms"
)

print(response.text)
@app.get('/')
def hello():
    return "Hola Amigo"

