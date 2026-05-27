from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime
from datetime import UTC, datetime
from app.database.base import Base

class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    price = Column(Numeric(10, 2))
    quantity = Column(Integer, default=0)
    
class Sale(Base):

    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity_sold = Column(Integer)
    total_price = Column(Numeric(10, 2))
    created_at = Column(DateTime(timezone=True), default=lambda:datetime.now(UTC))
    


