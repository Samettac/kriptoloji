def encrypt(metin):
    duz_alfabe = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    terse_alfabe = duz_alfabe[::-1]
    cipher_text = ""
    for karakter in metin:
        if karakter.isalpha():
            index = duz_alfabe.find(karakter)
            cipher_text += terse_alfabe[index]
        else:
            cipher_text += karakter
    return cipher_text


def decrypt(metin):
    return encrypt(metin)


sifrelenecek_metin = input("şifrelenecek metini girin: ").upper()
sifrelenmis = encrypt(sifrelenecek_metin)
print(sifrelenmis)
coz = decrypt(sifrelenmis)
print(coz)