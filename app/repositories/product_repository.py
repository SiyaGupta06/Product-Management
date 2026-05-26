from sqlalchemy.orm import Session
from app.database.models import Product

class ProductRepository:
    def get_all_products(self, db: Session):
        return db.query(Product).all()
    
    def get_product_by_name(self, db: Session, name: str):
        return db.query(Product).filter(Product.name == name).first()
    
    def add_product(self, db: Session, product: Product):
        
        product = Product(name=product.name, price=product.price, quantity=product.quantity)
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    def sell_product(self, db: Session, name: str, quantity: int):
        product = db.query(Product).filter(Product.name == name).first()
        if not product:
            return None
        if product.quantity < quantity:
            return None
        product.quantity -= quantity
        db.commit()
        db.refresh(product)
        return product
    
    def delete_product(self, db: Session, name: str):
        product = db.query(Product).filter(Product.name == name).first()
        if not product:
            return None
        db.delete(product)
        db.commit()
        return product
    
