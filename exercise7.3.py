angka = input("Masukkan sebuah angka: ")
angka2 = int(angka)

# Memeriksa apakah angka merupakan kelipatan 10 menggunakan operator modulo (%)
if angka2 % 10 == 0:
    print(f"Angka {angka2} adalah kelipatan 10.")
else:
    print(f"Angka {angka2} bukan kelipatan 10.")