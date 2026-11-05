p1 = {'hewan': 'Kucing', 'owner': 'Basthan'}
p2 = {'hewan': 'Anjing', 'owner': 'Yudi'}
p3 = {'hewan': 'Kelinci', 'owner': 'Basyara'}
pets = [p1, p2, p3]
for pet in pets:
    print(f"{pet['owner']} memiliki hewan peliharaan seekor {pet['hewan']}.")