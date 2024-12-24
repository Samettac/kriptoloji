def ean13_check(number):
    sum = 0
    for i in range(len(number)):
        digit = int(number[i])
        if i % 2 == 0:
            sum += digit
        else:
            sum += digit * 3

    kalan = sum % 10
    son_deger = 10 - kalan
    return son_deger

barkod = input("12 haneli barkodu girin: ")
print(barkod)
son_deger = ean13_check(barkod)
print(son_deger)
