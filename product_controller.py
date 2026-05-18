from product_service import ProductService


class ProductController:

    def __init__(self):
        self.service = ProductService()

    def show_products(self):
        self.service.show_all_products()

    def add_product(self):

        product_id = int(input("ID Barang: "))
        name = input("Nama Barang: ")
        price = int(input("Harga: "))
        category = input("Kategori: ")

        self.service.add_new_product(
            product_id,
            name,
            price,
            category
        )

    def confirm_sale(self):

        product_id = int(input("Masukkan ID Barang: "))

        self.service.sell_product(product_id)

    def delete_product(self):

        product_id = int(input("Masukkan ID Barang: "))

        self.service.remove_product(product_id)