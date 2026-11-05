g = {
    'variable': 'Wadah untuk menyimpan nilai data dalam memori.',
    'string': 'Urutan karakter atau teks yang diapit oleh tanda petik.',
    'list': 'Kumpulan item terurut yang isi elemennya bisa diubah.',
    'loop': 'Struktur perintah untuk mengeksekusi blok kode secara berulang.',
    'dictionary': 'Koleksi pasangan key-value untuk menyimpan data terhubung.',
    'boolean': 'Tipe data yang bernilai True atau False.',
    'tuple': 'Kumpulan item terurut yang nilainya tidak dapat diubah (immutable).',
    'float': 'Tipe data angka yang memiliki titik desimal.',
    'key': 'Pengenal unik dalam dictionary untuk mengakses nilainya.',
    'value': 'Nilai yang disimpan dan diasosiasikan dengan key dalam dictionary.',
}
for word, meaning in g.items():
    print(f"{word.title()}:\n\t{meaning}\n")