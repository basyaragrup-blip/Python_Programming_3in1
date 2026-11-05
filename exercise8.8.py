def make_album(artist_name, album_title):
    """Membuat dictionary yang mendeskripsikan album musik."""
    return {
        'artist': artist_name.title(),
        'title': album_title.title(),
    }
print("--- INPUT ALBUM FAVORIT ---")
print("(Ketik 'q' kapan saja untuk keluar)")
while True:
    artist = input("\nMasukkan nama artis: ")
    if artist.lower() == 'q':
        break
    title = input("Masukkan judul album: ")
    if title.lower() == 'q':
        break
    album_dict = make_album(artist, title)
    print(f"Hasil dictionary album: {album_dict}")