from app.database.db import Database


DB = Database("app/database/products.json")


class ProductRepository:

    def get_all_products(self):

        return DB.read()

    def save_products(self, products: dict):

        DB.write(products)