import store
import products

sprouts = store.Store("Sprouts")
print(sprouts.name)
sprouts.add_product("tomato")
sprouts.add_product("potato")
sprouts.add_product("eggs")
print(sprouts.list_of_products)
sprouts.sell_product(2)
broccoli = products.Products("broccoli", 2, "veggies")
apple = products.Products("apple", 3, "fruits")
sprouts.add_product(broccoli.name)
sprouts.add_product(apple.name)
print(sprouts.list_of_products)
broccoli.update_price(.5, .5).print_info()


# lettuce = Products("lettuce", 2, "veggies")
# print(lettuce)
# lettuce.update_price(.5, 3).print_info()
# broccoli = Products("broccoli", 1, "veggies")
# print(broccoli)
# broccoli.update_price(.5, .5).print_info()
# Sprouts.add_product(lettuce.name)
# Sprouts.add_product(broccoli.name)
# print(Sprouts.list_of_products)

