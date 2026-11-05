def kota(city, country='Indonesia'):
    """Mencetak lokasi kota beserta negaranya."""
    print(f"{city.title()} berada di negara {country.title()}.")
kota('surakarta')
kota('yogyakarta')
kota('reykjavik', 'iceland')