def bangun(first, last, **user_info):
    """Membuat dictionary berisi informasi profil pengguna."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
profile = bangun(
    'Muhammad', 
    'Basthan',
    location='Surakarta',
    field='Teknik Industri',
    university='UNS'
)
print(profile)