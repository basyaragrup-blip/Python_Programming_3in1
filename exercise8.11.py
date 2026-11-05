def kiriim(messages, sent_messages):
    """Mencetak pesan dan memindahkannya ke list sent_messages."""
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
kiriim(list[:], kirimlist)
print("\n--- STATUS LIST SETELAH PENGIRIMAN (DENGAN SLICE COPY) ---")
print(f"messages_list asli: {list}")
print(f"sent_messages_list: {kirimlist}")