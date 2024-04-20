meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            }

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print("kata yang dimaksud:", word)
    print(word, "artinya adalah", meme_dict[word])
    # Apa yang harus kita lakukan jika kata itu ditemukan?
else:
    print("gak tau")
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
