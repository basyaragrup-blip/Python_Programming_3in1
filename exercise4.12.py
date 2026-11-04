my_foods = ["bakso", "nasgor", "batagor"]
friend_foods = my_foods[:]
my_foods.append("Pempek")
friend_foods.append("eskirm")
print("Makanan favorit saya adalah:")
for food in my_foods:
    print(food)
print("\nMakanan favorit teman saya adalah:")
for food in friend_foods:
    print(food)