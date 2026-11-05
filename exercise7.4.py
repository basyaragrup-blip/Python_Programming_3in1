#pizza = "\nMasukkan topping pizza yang Anda inginkan:"
#pizza += "\n(Ketik 'quit' jika sudah selesai): "
#while True:
#    topping = input(pizza)
#    if topping.lower() == 'quit':
#        break
#    print(f"Saya akan menambahkan topping {topping} ke pizza Anda!")
topping = ""
while topping.lower() != 'quit':
    topping = input("Masukkan topping (ketik 'quit' untuk keluar): ")
    if topping.lower() != 'quit':
        print(f"Menambahkan {topping} ke pizza Anda!")