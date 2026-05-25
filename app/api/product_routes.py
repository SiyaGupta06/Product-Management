from fastapi import APIRouter

from app.models.product_model import Product
from app.services.product_service import ProductService


router = APIRouter()

service = ProductService()


@router.get("/products")
def view_products():

    return service.get_products()


@router.get("/product/{name}")
def get_product_by_name(name: str):

    return service.get_product(name)


@router.post("/product")
def add_product(product: Product):

    return service.add_product(product)


@router.put("/product/{name}")
def sell_product(name: str, quantity: int):

    return service.sell_product(name, quantity)


@router.delete("/product/{name}")
def delete_product(name: str):

    return service.delete_product(name)