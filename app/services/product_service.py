from fastapi import HTTPException

from app.repositories.product_repository import ProductRepository


repo = ProductRepository()


class ProductService:

    def get_products(self):

        products = repo.get_all_products()

        if not products:
            raise HTTPException(
                status_code=404,
                detail="No products found"
            )

        return products

    def get_product(self, name: str):

        products = repo.get_all_products()

        if name not in products:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        return products[name]

    def add_product(self, product):

        products = repo.get_all_products()

        if product.name in products:
            raise HTTPException(
                status_code=400,
                detail="Product already exists"
            )

        products[product.name] = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity
        }

        repo.save_products(products)

        return {
            "message": "Product added successfully"
        }

    def sell_product(self, name: str, quantity: int):

        products = repo.get_all_products()

        if name not in products:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        if products[name]["quantity"] < quantity:
            raise HTTPException(
                status_code=400,
                detail="Quantity insufficient"
            )

        products[name]["quantity"] -= quantity

        repo.save_products(products)

        return {
            "message": "Sold successfully"
        }

    def delete_product(self, name: str):

        products = repo.get_all_products()

        if name not in products:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        del products[name]

        repo.save_products(products)

        return {
            "message": "Product deleted successfully"
        }