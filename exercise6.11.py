kota = {
    'Surakarta': {
        'country': 'Indonesia',
        'population': '522.364',
        'fact': 'Dikenal sebagai kota budaya dan pusat kerajinan batik.',
    },
    'Tokyo': {
        'country': 'Jepang',
        'population': '13.960.000',
        'fact': 'Kawasan metropolitan terpadat di dunia.',
    },
    'Paris': {
        'country': 'Prancis',
        'population': '2.161.000',
        'fact': 'Terkenal dengan Menara Eiffel dan julukan Kota Cahaya.',
    },
}
for city, info in kota.items():
    print(f"Kota: {city}")
    print(f"  Negara   : {info['country']}")
    print(f"  Populasi : ±{info['population']}")
    print(f"  Fakta    : {info['fact']}\n")