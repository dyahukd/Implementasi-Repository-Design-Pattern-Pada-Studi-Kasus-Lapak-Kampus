class Product:

    def __init__(self, product_id, name, price, category, status):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.status = status

    def display(self):
        return f"{self.product_id} | {self.name} | Rp{self.price} | {self.category} | {self.status}"