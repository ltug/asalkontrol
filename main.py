for a in range(5):
    sayi = int(input(f"Sayı {a+1}'i girin"))
    if sayi > 1:
        for i in range(2,sayi):
            t = False
            if (sayi % i) == 0:
                print(sayi," asal sayı değildir")
                t = True
                break
        if t == False:
            print(sayi," asal sayıdır")
    else:
        print(sayi," asal sayı değildir")
