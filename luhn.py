def sum_of_digits(kart_no):
    sum = 0
    for i in range(len(kart_no)):
        digit = int(kart_no[i])
        print(digit)
        if i % 2 == 0:
            digit = digit * 2
            if digit > 9:
                x = (digit % 10) + (digit // 10)
                sum += x
                print(digit,x)
            else:
                sum += digit
        else:
            sum += digit
    return sum

def is_valid(kart_no):
    basamaklar_toplami = sum_of_digits(kart_no)
    print(basamaklar_toplami)
    if basamaklar_toplami % 10 == 0:
        print("Geçerli")
    else:
        print("Geçersiz")


kart_no = input("Kart numarası girin: ")
is_valid(kart_no)