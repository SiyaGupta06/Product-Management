from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from app.database.base import Base

class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    price = Column(Numeric(10, 2))
    quantity = Column(Integer, default=0)
    
    


