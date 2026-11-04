guests = [
    "Ibnu Sna", "Albert Einstein", "Nicola Tesla",
    "Nelson Mandela", "B.J. Habibie", "Tan Malaka",
] 
print("Maaf, meja baru tidak sampai tepat waktu. Hanya 2 orang yang bisa diundang.\n")
removed_guest = guests.pop()
print(f"Maaf {removed_guest}, saya tidak bisa mengundang Anda makan malam.")
removed_guest = guests.pop()
print(f"Maaf {removed_guest}, saya tidak bisa mengundang Anda makan malam.")
removed_guest = guests.pop()
print(f"Maaf {removed_guest}, saya tidak bisa mengundang Anda makan malam.")
removed_guest = guests.pop()
print(f"Maaf {removed_guest}, saya tidak bisa mengundang Anda makan malam.")
print(f"\nHalo {guests[0]}, Anda tetap diundang makan malam.")
print(f"Halo {guests[1]}, Anda tetap diundang makan malam.\n")
del guests[0]
del guests[0]
print(guests) 