kota = {
    'Surakarta': {
        'country': 'Indonesia',
        'population': 522364,
        'landmark': 'Keraton Surakarta',
        'fact': 'Pusat kebudayaan Jawa yang kaya akan sejarah dan kuliner.',
    },
    'Tokyo': {
        'country': 'Jepang',
        'population': 13960000,
        'landmark': 'Tokyo Tower',
        'fact': 'Gabungan harmoni antara tradisi kuno dan teknologi futuristik.',
    },
    'Paris': {
        'country': 'Prancis',
        'population': 2161000,
        'landmark': 'Menara Eiffel',
        'fact': 'Pusat seni, mode, dan kuliner internasional.',
    },
}
print("=" * 55)
print("             INFORMASI KOTA-KOTA DI DUNIA            ")
print("=" * 55)
for city, info in kota.items():
    print(f"\n[ {city.upper()} ]")
    print(f"  * Negara Asal    : {info['country']}")
    print(f"  * Estimasi Warga : {info['population']:,} jiwa")
    print(f"  * Landmark Utama : {info['landmark']}")
    print(f"  * Catatan Khusus : {info['fact']}")
    print("-" * 55)