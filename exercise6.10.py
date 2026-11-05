angka = {
    'Yapi': [7, 14, 21],
    'Kenza': [12, 99],
    'Haikal': [3],
    'AL': [42, 100, 777],
    'Nai': [5, 25],
}
for name, numbers in angka.items():
    num_str = ", ".join(str(n) for n in numbers)
    print(f"Angka favorit {name} adalah: {num_str}")