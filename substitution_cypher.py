alfabe = "abcdefghijklmnopqrstuvwxyz"
key =    "nutiyvxqflbcjrodhkaewspzgm"
plaintext = "samet"
# v! zmhvxdmxdmo!nll mikbg

def encrypt(plaintext, key):
    temp = ""
    for karakter in plaintext:
        if karakter.isalpha():
            temp += key[alfabe.index(karakter.lower())]
        else:
            temp += karakter
    return temp


def decrypt(cyphertext, key):
    temp = ""
    for karakter in cyphertext:
        if karakter.isalpha():
            temp += alfabe[key.index(karakter.lower())]
        else:
            temp += karakter
    return temp

print(encrypt(plaintext, key))
print(decrypt("anjye", key))

