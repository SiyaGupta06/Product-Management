from sqlalchemy.orm import Session
from app.database.models import Product
from app.database.models import Sale

class ProductRepository:
    def get_all_products(self, db: Session):
        return db.query(Product).all()
    
    def get_product_by_name(self, db: Session, name: str):
        if not db.query(Product).filter(Product.name == name).first():
            return "Product not found"
        return db.query(Product).filter(Product.name == name).first()
    
    def add_product(self, db: Session, product: Product):
        if db.query(Product).filter(Product.name == product.name).first():
            return "Product already exists"
        product = Product(id=product.id, name=product.name, price=product.price, quantity=product.quantity)
    
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    def sell_product(self, db: Session, name: str, quantity: int):
        product = db.query(Product).filter(Product.name == name).first()
        if not product:
            return "Product not found"
        if product.quantity < quantity:
            return "Insufficient quantity"
        product.quantity -= quantity
        
        sale = Sale(product_id=product.id, quantity_sold=quantity, total_price=product.price * quantity)
        db.add(sale)
        db.commit()
        db.refresh(product)
        return "Product sold successfully"
    
    def delete_product(self, db: Session, name: str):
        product = db.query(Product).filter(Product.name == name).first()
        if not product:
            return "Product not found"
        db.delete(product)
        db.commit()
        return "Product deleted successfully"
    
