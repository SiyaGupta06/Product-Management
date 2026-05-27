from fastapi import HTTPException

from app.repositories.product_repository import ProductRepository

from app.database.models import Product


repo = ProductRepository()


class ProductService:

    def get_products(self, db):

        return repo.get_all_products(db)

    def get_product_by_name(self, name, db):

        product = repo.get_product_by_name(
            db,
            name
        )

        if not product:

            raise HTTPException(

                status_code=404,

                detail="Product not found"
            )

        return product

    def add_product(self, product, db):

        existing_product = repo.get_product_by_name(
            db,
            product.name
        )

        if existing_product:

            raise HTTPException(

                status_code=400,

                detail="Product already exists"
            )

        new_product = Product(

            id=product.id,

            name=product.name,

            price=product.price,

            quantity=product.quantity
        )

        return repo.create_product(db, new_product)

    def delete_product(self, name, db):

        product = repo.get_product_by_name(
            db,
            name
        )

        if not product:

            raise HTTPException(

                status_code=404,

                detail="Product not found"
            )

        return repo.delete_product(db, product)
