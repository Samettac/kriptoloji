def iban_check(iban):
    ilk_dort = iban[4:] + iban[:4]
    char_to_digit = ""
    for char in ilk_dort:
        if char.isdigit():
            char_to_digit += str(char)
        else:
            char_to_digit += str(ord(char.upper()) - ord("A") + 10)
    mod = int(char_to_digit) % 97
    return mod

iban = input("Enter")
print(iban)
kalan = iban_check(iban)
print(kalan)
