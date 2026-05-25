from fastapi import FastAPI

from app.api.product_routes import router


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Product Management API!"}



app.include_router(router)