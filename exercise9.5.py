class Pengguna:
    def __init__(self, nama_depan, nama_belakang, nama_pengguna, surel):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nama_pengguna = nama_pengguna
        self.surel = surel
        self.percobaan_masuk = 0
    def deskripsikan_pengguna(self):
        print(f"Profil Pengguna: {self.nama_depan} {self.nama_belakang}")
        print(f"- Nama Pengguna: {self.nama_pengguna}")
        print(f"- Surel: {self.surel}")
    def sapa_pengguna(self):
        print(f"Selamat datang kembali, bro {self.nama_depan}!")
    def tambah_percobaan_masuk(self):
        self.percobaan_masuk += 1
    def atur_ulang_percobaan_masuk(self):
        self.percobaan_masuk = 0
pengguna_bas = Pengguna('Basthan', 'Basyara', 'bas_b', 'bas@example.com')
pengguna_bas.tambah_percobaan_masuk()
pengguna_bas.tambah_percobaan_masuk()
pengguna_bas.tambah_percobaan_masuk()
pengguna_bas.tambah_percobaan_masuk()
print(f"Jumlah percobaan masuk: {pengguna_bas.percobaan_masuk}")
pengguna_bas.atur_ulang_percobaan_masuk()
print(f"Jumlah percobaan masuk setelah diatur ulang: {pengguna_bas.percobaan_masuk}")