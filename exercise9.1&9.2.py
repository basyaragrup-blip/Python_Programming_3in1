class Restoran:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan

    def deskripsikan_restoran(self):
        print(f"Nama Restoran: {self.nama_restoran}")
        print(f"Jenis Masakan: {self.jenis_masakan}")

    def buka_restoran(self):
        print(f"{self.nama_restoran} sekarang sudah buka!")

restoran = Restoran("Warung Sederhana", "Padang")
print(restoran.nama_restoran)
print(restoran.jenis_masakan)
restoran.deskripsikan_restoran()
restoran.buka_restoran()
print("-" * 20)

restoran_1 = Restoran("Sushitei", "Jepang")
restoran_2 = Restoran("Pizza Hut", "Italia")
restoran_3 = Restoran("KFC", "Amerika")

restoran_1.deskripsikan_restoran()
print("-" * 10)
restoran_2.deskripsikan_restoran()
print("-" * 10)
restoran_3.deskripsikan_restoran()