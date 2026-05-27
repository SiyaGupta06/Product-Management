from fastapi import FastAPI

from app.api.product_routes import router as product_router
from app.api.sale_routes import router as sale_router


app = FastAPI()


app.include_router(product_router)
app.include_router(sale_router)