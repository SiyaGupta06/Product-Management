from app.database.models import Product


class ProductRepository:

    def get_all_products(self, db):

        return db.query(Product).all()

    def get_product_by_name(self, db, name):

        return db.query(Product).filter(
            Product.name == name
        ).first()

    def create_product(self, db, product):

        db.add(product)

        db.commit()

        db.refresh(product)

        return "Product added successfully"

    def update_product(self, db):

        db.commit()

    def delete_product(self, db, product):

        db.delete(product)

        db.commit()
        return "Product deleted successfully"