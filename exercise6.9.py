tempat = {
    'Basthan': ['Pantai Kuta', 'Candi Borobudur'],
    'Yapi': ['Gunung Bromo'],
    'Budi': ['Malioboro', 'Danau Toba', 'Taman Mini'],
}
for name, places in tempat.items():
    if len(places) == 1:
        print(f"Tempat favorit {name} adalah:")
    else:
        print(f"Tempat-tempat favorit {name} adalah:")
    for place in places:
        print(f"  - {place}")
    print()