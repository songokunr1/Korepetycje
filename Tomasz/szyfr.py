kod = "patetyr śoin e wimra ęejzdneai"

# 1-40
# wypisz po zamianie
# for przesuniecie in range(-40, 40):
#     zdanie = ''
#     for literka in kod:
#         liczba = ord(literka) + przesuniecie
#         nowa_literka = chr(liczba)
#         zdanie =zdanie + nowa_literka
#     print(zdanie)
#     # liczba_asci = literka -> na kod asci
#     # liczba_asci = liczba_asci +1 potem -> dodajemy do niego 1
#     # funkcje_zaminay(liczba_asci), zmiana  +1 na znak
#     # i dodanie tej zmiennej do zdanie # zdanie = zdanie +  funkcje_zaminay(liczba_asci)

for liczba in range(len(kod)):
    rozszyfrowane = ''
    for liczba_2 in range(len(kod)):
            rozszyfrowane = rozszyfrowane + kod[(liczba+liczba_2)%len(kod)]
    print(rozszyfrowane)