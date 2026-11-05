def city_country(city, country):
    """Mengembalikan nama kota dan negara yang diformat rapat."""
    return f"{city.title()}, {country.title()}"
l1 = city_country('santiago', 'chile')
l2 = city_country('tokyo', 'japan')
l3 = city_country('jakarta', 'indonesia')

# Mencetak nilai return
print(l1)
print(l2)
print(l3)