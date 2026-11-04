guests = ["Albert Einstein", "Nicola Tesla", "Soedirman"]

print(f"Halo {guests[0]}, maukah Anda makan malam bersama saya?")
print(f"Halo {guests[1]}, maukah Anda makan malam bersama saya?")
print(f"Halo {guests[2]}, maukah Anda makan malam bersama saya?")

# Tamu yang tidak bisa hadir
print(f"\nSayang sekali, {guests[2]} tidak bisa hadir.\n")

# Mengganti elemen dengan menimpa nilai pada indeksnya
guests[2] = "B.J. Habibie"

print(f"Halo {guests[0]}, maukah Anda makan malam bersama saya?")
print(f"Halo {guests[1]}, maukah Anda makan malam bersama saya?")
print(f"Halo {guests[2]}, maukah Anda makan malam bersama saya?")