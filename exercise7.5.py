tiket = "\nMasukkan usia Anda untuk mengecek harga tiket:"
tiket += "\n(Ketik 'quit' untuk keluar): "
while True:
    age_input = input(tiket)
    if age_input.lower() == 'quit':
        break
    age = int(age_input)
    if age < 3:
        print("Tiket gratis untuk Anda!")
    elif age <= 12:
        print("Harga tiket Anda adalah $10.")
    else:
        print("Harga tiket Anda adalah $15.")