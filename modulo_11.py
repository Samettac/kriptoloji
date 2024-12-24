def sum_of_digits(sayi):
    sum = 0
    weights = list(range(len(sayi), 0, -1))
    for i in range(len(sayi)):
        digit = int(sayi[i])
        carpim = digit * weights[i]
        sum += carpim
    return sum


def is_valid(sayi):
    agirlikli_toplam = sum_of_digits(sayi)
    print(agirlikli_toplam)
    if agirlikli_toplam % 11 == 0:
        print("Geçerli")
    else:
        print("Geçersiz")


sayi = input("sayi girin: ")
is_valid(sayi)