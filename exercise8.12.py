def buat(*items):
    """Mencetak ringkasan bahan-bahan sandwich yang dipesan."""
    print("\nMembuat sandwich dengan isian berikut:")
    for item in items:
        print(f"- {item}")
buat('keju', 'daging sapi')
buat('tuna', 'selada', 'tomat')
buat('ayam', 'telur', 'mayones', 'saus sambal')