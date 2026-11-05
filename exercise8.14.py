def buat(manufacturer, model, **info):
    """Membuat dictionary berisi seluruh spesifikasi mobil."""
    info['manufacturer'] = manufacturer
    info['model'] = model
    return info
mobil = buat('subaru', 'outback', color='blue', tow_package=True)
print(mobil)