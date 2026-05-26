from fastapi import HTTPException

from app.repositories.product_repository import ProductRepository


repo = ProductRepository()


class ProductService:

    def get_products(self, db):

        return repo.get_all_products(db)

    def get_product_by_name(self, name: str, db):
        
        product = repo.get_product_by_name(db, name)
        
        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        return product

    def add_product(self, product, db):

        products = repo.get_product_by_name(db, product)

        if product.name in products:
            raise HTTPException(
                status_code=400,
                detail="Product already exists"
            )


        repo.add_product(db, product)

        return {
            "message": "Product added successfully"
        }

    def sell_product(self, name: str, quantity: int, db):

        product = repo.get_product_by_name(db, name)

        if  not  product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        if product.quantity < quantity:
            raise HTTPException(
                status_code=400,
                detail="Quantity insufficient"
            )

        product.quantity -= quantity

        db.commit()
        db.refresh(product)


        return {
            "message": "Sold successfully"
        }

    def delete_product(self, name, db):

        product = repo.get_product_by_name(db, name)

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        repo.delete_product(db, product)

        db.commit()
        db.refresh(product)


        return {
            "message": "Product deleted successfully"
        }