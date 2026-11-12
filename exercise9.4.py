class Restoran:
    def __init__(self, nama_restoran, jenis_masakan):
        self.nama_restoran = nama_restoran
        self.jenis_masakan = jenis_masakan
        self.jumlah_dilayani = 0

    def deskripsikan_restoran(self):
        print(f"Restoran {self.nama_restoran} menyajikan masakan {self.jenis_masakan}.")
    def buka_restoran(self):
        print(f"Restoran {self.nama_restoran} sekarang buka!")
    def atur_jumlah_dilayani(self, jumlah):
        self.jumlah_dilayani = jumlah
    def tambah_jumlah_dilayani(self, tambahan_pelanggan):
        self.jumlah_dilayani += tambahan_pelanggan
restoran_padang = Restoran('Warung Sederhana', 'Padang')
print(f"Jumlah pelanggan awal: {restoran_padang.jumlah_dilayani}")
restoran_padang.jumlah_dilayani = 15
print(f"Jumlah pelanggan (diubah langsung): {restoran_padang.jumlah_dilayani}")
restoran_padang.atur_jumlah_dilayani(30)
print(f"Jumlah pelanggan (metode atur): {restoran_padang.jumlah_dilayani}")
restoran_padang.tambah_jumlah_dilayani(45)
print(f"Jumlah total pelanggan (setelah ditambah): {restoran_padang.jumlah_dilayani}")