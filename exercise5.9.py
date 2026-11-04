usns = []
if usns:
    for username in usns:
        if username == 'admin':
            print("Halo admin, apakah Anda ingin melihat laporan status?")
        else:
            print(f"Halo {username.title()}, terima kasih telah login kembali.")
else:
    print("Kita perlu mencari beberapa pengguna!")