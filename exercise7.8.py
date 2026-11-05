pesanan = ['tuna', 'turkey', 'club', 'keju']
akhir = []
while pesanan:
    current_sandwich = pesanan.pop(0)
    print(f"Saya telah membuat sandwich {current_sandwich} Anda.")
    akhir.append(current_sandwich)
print("\nBerikut daftar sandwich yang telah selesai dibuat:")
for sandwich in akhir:
    print(f"- Sandwich {sandwich.title()}")