from fastapi import HTTPException

from app.repositories.product_repository import ProductRepository

from app.repositories.sale_repository import SaleRepository

from app.database.models import Sale


product_repo = ProductRepository()

sale_repo = SaleRepository()


class SaleService:

    def sell_product(
        self,
        name,
        quantity,
        db
    ):

        product = product_repo.get_product_by_name(
            db,
            name
        )

        if not product:

            raise HTTPException(

                status_code=404,

                detail="Product not found"
            )

        if product.quantity < quantity:

            raise HTTPException(

                status_code=400,

                detail="Insufficient quantity"
            )

        product.quantity -= quantity

        product_repo.update_product(db)

        sale = Sale(

            product_id=product.id,

            quantity_sold=quantity,

            total_price=product.price * quantity
        )

        

        return sale_repo.create_sale(db, sale)