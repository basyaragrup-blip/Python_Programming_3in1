respon = {}
polling = True

while polling:
    name = input("Siapa nama Anda? ")
    place = input("Jika Anda bisa mengunjungi satu tempat di dunia, ke mana Anda ingin pergi? ")
    respon[name] = place
    
    repeat = input("Apakah ada orang lain yang ingin mengisi survei? (ya/tidak): ")
    if repeat.lower().strip() == 'tidak':
        polling = False  # Diubah dari polling_active menjadi polling

print("\n--- HASIL SURVEI LIBURAN IMPIAN ---")
for name, place in respon.items():
    print(f"{name.title()} ingin mengunjungi {place.title()}.")