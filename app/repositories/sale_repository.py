from app.database.models import Sale


class SaleRepository:

    def create_sale(self, db, sale):

        db.add(sale)

        db.commit()

        db.refresh(sale)

        return "Sale recorded successfully"