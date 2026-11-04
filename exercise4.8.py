# Latihan 4.8: Cubes
# Membuat list 10 kubus pertama, lalu mencetak tiap nilainya.
cubes = []
for number in range(1, 11):
    cubes.append(number ** 3)
for cube in cubes:
    print(cube)