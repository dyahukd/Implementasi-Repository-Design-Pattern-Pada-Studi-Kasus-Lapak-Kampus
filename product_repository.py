from database import products_db


class ProductRepository:

    def get_all_products(self):
        return products_db

    def get_product_by_id(self, product_id):

        for product in products_db:

            if product.product_id == product_id:
                return product

        return None

    def add_product(self, product):
        products_db.append(product)

    def update_product_status(self, product_id, status):

        product = self.get_product_by_id(product_id)

        if product:
            product.status = status
            return True

        return False

    def delete_product(self, product_id):

        product = self.get_product_by_id(product_id)

        if product:
            products_db.remove(product)
            return True

        return False