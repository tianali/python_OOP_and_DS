class Store:
    def __init__(self, name):
        self.name = name
        self.list_of_products = []

    def add_product(self, new_product):
        self.list_of_products.append(new_product)
        return self

    def sell_product(self, id):
        self.list_of_products.pop()
        print (self.list_of_products)
        return self






