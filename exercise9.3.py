class Pengguna:
    def __init__(self, nama_depan, nama_belakang, usia, lokasi, pekerjaan):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.usia = usia
        self.lokasi = lokasi
        self.pekerjaan = pekerjaan

    def deskripsikan_pengguna(self):
        print(f"Ringkasan Profil:")
        print(f"- Nama: {self.nama_depan.title()} {self.nama_belakang.title()}")
        print(f"- Usia: {self.usia} tahun")
        print(f"- Lokasi: {self.lokasi.title()}")
        print(f"- Pekerjaan: {self.pekerjaan.title()}")

    def sapa_pengguna(self):
        print(f"Halo {self.nama_depan.title()}, selamat datang kembali!")
pengguna_1 = Pengguna("budi", "santoso", 28, "jakarta", "insinyur perangkat lunak")
pengguna_2 = Pengguna("siti", "aminah", 24, "surabaya", "desainer grafis")
pengguna_3 = Pengguna("andi", "wijaya", 35, "bandung", "manajer proyek")

pengguna_1.deskripsikan_pengguna()
pengguna_1.sapa_pengguna()
print("-" * 20)

pengguna_2.deskripsikan_pengguna()
pengguna_2.sapa_pengguna()
print("-" * 20)

pengguna_3.deskripsikan_pengguna()
pengguna_3.sapa_pengguna()