from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.models.product_model import Product
from app.services.product_service import ProductService


router = APIRouter()

service = ProductService()

def get_db():
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/products")
def view_products(db: Session = Depends(get_db)):

    return service.get_products(db)


@router.get("/product/{name}")
def get_product_by_name(name: str, db: Session = Depends(get_db)):

    return service.get_product_by_name(name, db)


@router.post("/product")
def add_product(product: Product, db: Session = Depends(get_db)):

    return service.add_product(product, db)


@router.put("/product/{name}")
def sell_product(name: str, quantity: int, db: Session = Depends(get_db)):

    return service.sell_product(name, quantity, db)


@router.delete("/product/{name}")
def delete_product(name: str, db: Session = Depends(get_db)):

    return service.delete_product(name, db)