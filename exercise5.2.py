fruit = 'apple'
print("Pengujian kesamaan string (True):", fruit == 'apple')
print("Pengujian ketidaksamaan string (False):", fruit != 'apple')
name = 'JOHN'
print("\nPengujian method lower() (True):", name.lower() == 'john')
print("Pengujian method lower() (False):", name.lower() == 'JOHN')
age = 21
print("\nNumerik sama dengan (True):", age == 21)
print("Numerik tidak sama dengan (False):", age != 21)
print("Numerik lebih besar dari (True):", age > 18)
print("Numerik lebih kecil dari (False):", age < 18)
print("Numerik lebih besar atau sama dengan (True):", age >= 21)
print("Numerik lebih kecil atau sama dengan (False):", age <= 20)
score = 85
print("\nPengujian dengan 'and' (True):", score > 80 and score < 90)
print("Pengujian dengan 'and' (False):", score > 80 and score > 90)
print("Pengujian dengan 'or' (True):", score == 85 or score == 100)
print("Pengujian dengan 'or' (False):", score == 90 or score == 100)
toppings = ['mushrooms', 'onions', 'pineapple']
print("\nItem ada di dalam list (True):", 'mushrooms' in toppings)
print("Item ada di dalam list (False):", 'pepperoni' in toppings)
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
print("\nItem tidak ada di dalam list (True):", user not in banned_users)
print("Item tidak ada di dalam list (False):", 'andrew' not in banned_users)