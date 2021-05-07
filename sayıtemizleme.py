def SayiTemizleme():
    a = "1234567890"
    ilk_string ="Ah5me4t"
    for i in a:
        ilk_string = ilk_string.replace(i, "")
    ikinci_string = "M9eHm4eT"
    for i in a:
        ikinci_string = ikinci_string.replace(i, "")
    ucuncu_string ="Ha3K5a1n"
    for i in a:
        ucuncu_string = ucuncu_string.replace(i, "")
    Birlesmis_deger="-".join([ilk_string,ikinci_string,ucuncu_string])
    print(Birlesmis_deger)
    return Birlesmis_deger
SayiTemizleme()