fav = {
    'Bas': 'python',
    'Basyara': 'c',
    'Ken': 'rust',
    'Yapi': 'python',
}
people_to_poll = ['Bas', 'Basyara', 'ken', 'Yapi', 'Agus', 'Yanto']
for person in people_to_poll:
    if person in fav:
        print(f"Terima kasih, {person.title()}, karena sudah berpartisipasi dalam survei!")
    else:
        print(f"Halo, {person.title()}, yuk luangkan waktu sebentar untuk mengisi survei kami!")