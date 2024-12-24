def encrypt(plaintext, a, b):
    ciphertext = ""
    mod = 26
    for karakter in plaintext:
        if karakter.isalpha():
            if karakter.isupper():
                x = ord(karakter) - 65
                yeni_deger = (a * x) + b
                ciphertext += chr(yeni_deger % mod + 65)
            else:
                #print(ord(karakter))
                x = ord(karakter) - 97
                #print(x)
                yeni_deger = (a * x) + b
                #print(yeni_deger)
                ciphertext += chr(yeni_deger % mod + 97)
        else:
            ciphertext += karakter
    return ciphertext


def decrypt(ciphertext, a, b):
    plaintext = ""
    mod = 26
    a_tersi = pow(a, -1, mod)
    for karakter in ciphertext:
        if karakter.isalpha():
            if karakter.isupper():
                y = ord(karakter) - 65
                yeni_deger = ((y-b) * a_tersi) % mod
                plaintext += chr(yeni_deger + 65)
            else:
                y = ord(karakter) - 97
                yeni_deger = ((y - b) * a_tersi) % mod
                plaintext += chr(yeni_deger + 97)
        else:
            plaintext += karakter
    return plaintext



plaintext = input("Şifrelenecek metini giriniz: ")
a_degeri = int(input("a değerini giriniz: "))
b_degeri = int(input("b değerini giriniz: "))

x = encrypt(plaintext, a_degeri, b_degeri)

print(plaintext)
print(a_degeri, b_degeri)
print(x)

print(decrypt(x, a_degeri, b_degeri))