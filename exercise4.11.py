# Latihan 4-11: My Pizzas, Your Pizzas
# Membuat salinan list, lalu menambah item ke masing-masing list.
pizzas = ["pepperoni", "margherita", "hawaiian"]
friend_pizzas = pizzas[:]
pizzas.append("four cheese")
friend_pizzas.append("bbq chicken")
print("Pizza favorit saya adalah:")
for pizza in pizzas:
    print(pizza)
print("\nPizza favorit teman saya adalah:")
for pizza in friend_pizzas:
    print(pizza)