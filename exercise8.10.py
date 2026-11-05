def kirim(messages, sent_messages):
    """
    Mencetak setiap pesan, lalu memindahkannya dari list 'messages'
    ke dalam list 'sent_messages'.
    """
    while messages:
        pesanjuga = messages.pop(0)
        print(f"Mengirim pesan: {pesanjuga}")
        sent_messages.append(pesanjuga)
list = [
    "Halo, apa kabar?",
    "Jangan lupa latihan coding hari ini!",
    "Sampai jumpa di pertemuan berikutnya."
]
kirimlist = []
kirim(list, kirimlist)
print("\n--- STATUS LIST SETELAH PENGIRIMAN ---")
print(f"messages_list     : {list}")
print(f"sent_messages_list: {kirimlist}")