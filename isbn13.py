def isbn_13(isbn):
    sum = 0
    for i in range(len(isbn)):
        digit = int(isbn[i])
        if i % 2 == 0:
            sum += digit
        else:
            sum += 3 * digit
    return sum

def is_valid(isbn):
    agirlikli_toplam = isbn_13(isbn)
    print(agirlikli_toplam)
    if agirlikli_toplam % 10 == 0:
        print("Geçerli")
    else:
        print("Geçersiz")

isbn = input("ISBN DEGERİ: ")
print(isbn)
is_valid(isbn)