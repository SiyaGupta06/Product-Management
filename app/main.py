from fastapi import FastAPI

from app.api.product_routes import router


app = FastAPI()




app.include_router(router)