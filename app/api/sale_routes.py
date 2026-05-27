from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.services.sale_service import SaleService


router = APIRouter()
service = SaleService()


@router.put("/product/{name}")
def sell_product(name: str, quantity: int, db: Session = Depends(get_db)):

    return service.sell_product(name, quantity, db)