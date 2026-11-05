def make_album(artist_name, album_title, songs=None):
    """Membuat dictionary yang mendeskripsikan album musik."""
    album = {
        'artist': artist_name.title(),
        'title': album_title.title(),
    }
    if songs:
        album['songs'] = songs
    return album
album1 = make_album('coldplay', 'parachutes')
album2 = make_album('taylor swift', '1989')
album3 = make_album('sheila on 7', 'kisah klasik untuk masa depan')
album4 = make_album('feast', 'membangun dan merusak', songs=11)
print(album1)
print(album2)
print(album3)
print(album4)