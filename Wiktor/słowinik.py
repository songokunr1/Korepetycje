# slownik = {1 : "poniedzialek", 2 : "wtorek" , 3 : "sroda" , 4 : "czwartek" , 5 : "piatek" , 6 : "sobota" , 7 : "niedziela"}
# # slownik["Pawel"] = 50
# for element in range(1,8):
#     print(str(element) + " - " + str(slownik[element]))
#
#
# for key,value in slownik.items():
#     print(key, value)
#
#
# for key in slownik.keys():
#     print(key)
#
# for value in slownik.values():
#     print(value)

{'styczen': {zarobek dzienny: x, zarobek_tygodniowy, zarobek_miesieczny, wydatki, stan_konta_na_koniec_miesiąca},
 'luty': {zarobek dzienny: x, zarobek_tygodniowy, zarobek_miesieczny, wydatki, stan_konta_na_koniec_miesiąca},},

# wiktor dostaje kiepszonkowe w parzysty dzien tygodnia (2zl)
# kazdego miesiaca dostaje plus 1zl na dzien tylko w parzyste
# a kazdego tygodnia dostaje 10zl za nauke ppythona.
# w styczniu wiktor sprzedal koputer za 550 zl
# a w czerwcu byl na wakacjach i wydal 200zl
#
# stworz slownik gdzie zobaczysz ile w danym miesiacu/ Witkor bedzie mial kasy.
miesiace = {1 : "styczen", 2 : "luty" ,3 : "marzec", 4 : "kwiecien", 5 : "maj", 6 : "czerwiec", 7 : "lipiec", 8 : "sierpien", 9 : "wrzesien", 10 : "listopad",11 : "pazdziernik", 12 : "grudzien"}
zarobek_dzienny = 2
zarobek_miesieczny = 0
zarobek_roczny = {}
stan_konta = 0
kasa = {}
for miesiac in range (1,13):
    zarobek_miesieczny = 0
    for tydzień in range(1,5):
        for dzien in range(1,8):
            if dzien%2 == 0:
                zarobek_miesieczny = zarobek_dzienny + zarobek_miesieczny
        zarobek_miesieczny = zarobek_miesieczny + 10
    if miesiac == 1:
        zarobek_miesieczny = zarobek_miesieczny + 550
    if miesiac == 6:
        zarobek_miesieczny = zarobek_miesieczny - 200
    zarobek_dzienny += 1
    stan_konta = stan_konta + zarobek_miesieczny

    # wersja podstawowa

    # print(zarobek_miesieczny)
    # sl2 = {"dochod" : zarobek_miesieczny, "stan konta" : stan_konta}
    # zarobek_roczny[miesiace[miesiac]] = sl2
    # print(zarobek_roczny)


    # Wersja bardziej przejżysta

    sl2 = {"dochod" : zarobek_miesieczny, "stan konta" : stan_konta}
    kasa[miesiac] = sl2
    dane = (str(miesiace[miesiac]) + " ---> " + str(kasa[miesiac]))
    print("\n")
    print(dane.center(200," "))


    # portfel = {
    #     'Styczen': {'dochod': wyliczyc
    #                 'stan_konta': stan_konta_napoprzedni_miesiac + dodac dochod}
    # }


