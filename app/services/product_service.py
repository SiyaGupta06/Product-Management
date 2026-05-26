from fastapi import HTTPException

from app.repositories.product_repository import ProductRepository


repo = ProductRepository()


class ProductService:

    def get_products(self, db):

        return repo.get_all_products(db)

    def get_product_by_name(self, name: str, db):
        
        return repo.get_product_by_name(db, name)

    def add_product(self, product, db):

        return repo.add_product(db, product)

    def sell_product(self, name: str, quantity: int, db):

       return repo.sell_product(db, name, quantity)


    def delete_product(self, name, db):

        return repo.delete_product(db, name)


       