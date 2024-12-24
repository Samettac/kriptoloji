
def sezar_kriptolama(metin, kaydirma):
    kriptolanmis_metin = ""
    for karekter in metin:
        if karekter.isalpha():
            if karekter.isupper():
                sifrelenmis_deger = (((ord(karekter) - 65) + kaydirma) % 26)
                kriptolanmis_metin += chr(sifrelenmis_deger + 65)
            else:
                sifrelenmis_deger = (((ord(karekter) - 97) + kaydirma) % 26)
                kriptolanmis_metin += chr(sifrelenmis_deger + 97)
        else:
            kriptolanmis_metin += karekter
    return kriptolanmis_metin

def sezar_coz(metin, kaydirma):
    cozulmus_metin = ""
    for karekter in metin:
        if karekter.isalpha():
            if karekter.isupper():
                cozulmus_deger = ((ord(karekter) - 65 - kaydirma) % 26)
                cozulmus_metin += chr(cozulmus_deger + 65)
            else:
                cozulmus_deger = ((ord(karekter) - 97 - kaydirma) % 26)
                cozulmus_metin += chr(cozulmus_deger + 97)
        else:
            cozulmus_metin += karekter
    return cozulmus_metin

kriptolanacak_metin = input("kriptolanacak metini giriniz: ")
kaydirma_degeri = int(input("kaydirma degeri girinişz (1-25): "))

print(kriptolanacak_metin)
print(kaydirma_degeri)

kriptolanmis_metin = sezar_kriptolama(metin=kriptolanacak_metin, kaydirma=kaydirma_degeri)
print(kriptolanmis_metin)

cozulmus_metin = sezar_coz(metin=kriptolanmis_metin, kaydirma=kaydirma_degeri)
print(cozulmus_metin)










