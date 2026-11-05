def buat(*items):
    """Mencetak ringkasan bahan-bahan sandwich yang dipesan."""
    print("\nMembuat sandwich dengan isian:")
    for item in items:
        print(f"- {item}")