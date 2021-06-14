class Products:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased > self.price:
            self.price += self.price * percent_change 
            print("Increased in price")
            print(self.name, "has increased in price to ", self.price)
        if is_increased < self.price:
            self.price -= self.price * percent_change
            print(self.name, "has decreased in price to ", self.price)
        return self

    def print_info(self):
        print("Product: ", self.name, "/ Category: ", self.category, "/ Price: ", self.price)