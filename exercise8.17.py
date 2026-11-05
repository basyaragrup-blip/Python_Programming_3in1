def display_message():
    """Mencetak penjelasan materi yang sedang dipelajari."""
    print("Saya sedang belajar menerapkan panduan PEP 8 pada fungsi Python.")

def make_shirt(size='L', text='I Love Python'):
    """Membuat kaos dengan ukuran dan pesan yang dapat disesuaikan."""
    print(f"Membuat kaos ukuran {size} dengan tulisan '{text}'.")

def describe_city(city, country='Indonesia'):
    """Mencetak informasi lokasi kota beserta negaranya."""
    print(f"{city.title()} berada di negara {country.title()}.")

display_message()
print()

make_shirt()
make_shirt(size='M')
make_shirt(size='S', text='Logic First')
print()

describe_city('surakarta')
describe_city('yogyakarta')
describe_city('reykjavik', 'iceland')