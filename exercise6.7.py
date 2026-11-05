p1 = {
    'awal': 'Budi',
    'akhir': 'Santoso',
    'umur': 20,
    'kota': 'Surakarta',
}
p2 = {
    'awal': 'Nabila',
    'akhir': 'Aminah',
    'umur': 21,
    'kota': 'Yogyakarta',
}
p3 = {
    'awal': 'Andi',
    'akhir': 'Pratama',
    'umur': 19,
    'kota': 'Semarang',
}
orang = [p1, p2, p3]
for person in orang:
    full_name = f"{person['awal']} {person['akhir']}"
    print(f"Nama Lengkap : {full_name}")
    print(f"Umur         : {person['umur']} tahun")
    print(f"Kota         : {person['kota']}\n")