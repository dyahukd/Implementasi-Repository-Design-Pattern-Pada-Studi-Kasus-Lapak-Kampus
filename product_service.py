from product import Product
from product_repository import ProductRepository


class ProductService:

    def __init__(self):
        self.repository = ProductRepository()

    def show_all_products(self):

        products = self.repository.get_all_products()

        print("\n=== DAFTAR BARANG ===")

        for product in products:
            print(product.display())

    def add_new_product(self, product_id, name, price, category):

        new_product = Product(
            product_id,
            name,
            price,
            category,
            "Available"
        )

        self.repository.add_product(new_product)

        print("\nBarang berhasil ditambahkan")

    def sell_product(self, product_id):

        success = self.repository.update_product_status(
            product_id,
            "Sold"
        )

        if success:
            print("\nStatus barang berhasil diubah menjadi SOLD")
        else:
            print("\nBarang tidak ditemukan")

    def remove_product(self, product_id):

        success = self.repository.delete_product(product_id)

        if success:
            print("\nBarang berhasil dihapus")
        else:
            print("\nBarang tidak ditemukan")