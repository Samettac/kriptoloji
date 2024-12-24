def encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    for i in range(len(plaintext)):
        mod_index = i % len(key)
        karakter = plaintext[i]
        if karakter.isalpha():
            kaydirma = ord(key[mod_index]) - 65
            ascii_degeri = ord(plaintext[i])
            if karakter.isupper():
                y = (ascii_degeri - ord("A") + kaydirma) % 26
                sifreli_karakter = chr(y + ord("A"))
                ciphertext += sifreli_karakter
                #print(sifreli_karakter)
            else:
                y = (ascii_degeri - ord("a") + kaydirma) % 26
                ciphertext += chr(y + ord("a"))
        else:
            ciphertext += karakter
    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    for i in range(len(ciphertext)):
        mod_index = i % len(key)
        karakter = ciphertext[i]
        if karakter.isalpha():
            kaydirma = ord(key[mod_index]) - 65
            if karakter.isupper():
                plaintext += chr((ord(karakter) - 65 - kaydirma) % 26 + 65)
            else:
                plaintext += chr((ord(karakter) - 97 - kaydirma) % 26 + 97)
        else:
            plaintext += karakter
    return plaintext


metin = input("Şifrelenecek metini girin: ")
key = input("Anahtarı girin: ")

print(metin, key)

kriptolanmis = encrypt(metin, key)
print(kriptolanmis)
cozulmus = decrypt(kriptolanmis, key)
print(cozulmus)