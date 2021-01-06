#
# Przeszukiwania:
# Liniowy:
# [3,5,7,2,1,21,12,23,8]
#
# binarne:
# [1,2,3,6,9,22,33,64,88]
# 0: szukamy 2
# 1:posortowane:
# 2: wybieramy środkową liczbę
#   jezeli x == 2 to konczymy
#   jezeli x>2:
#    # to odrzucamy wszystko po prawej i powtarzamy przeszukiwanie po lewej stronie
#   jezeli x<2:
# # to odrzucamy wszystko po lewej i powtarzamy przeszukiwanie po prawej stronie
#
#
# sortowania: przez wybór
# [3,5,7,21,12,23,8]
# [1,2]
#
# sortowanie przez zamianę:
# [3,5,7,2,1,21,12,23,8]
#
# quick sort:
# [3,5,7,2,1,21,12,23,8]
# i j zmienne pomocniczne, min i maxima
#
# sorotwanie babelkowe: porówanie dwóch liczb ze sobą
# [3,5,2,1,7,21,12,23,8]
#
#
# Sito Eratostenesa - przeszukiwanie liczb pierwszych
# 1,2,3,/4,5,/6,7,/8,9...                  do 21:
# 2, tak wiec usuwam 4,6,8
# 3, tak wiec usuwam 6 9 12
# i tak dalej i tak dalej
#
#
# Algorytm Euklidesa:
# Najwieszy wspolny dzielnik:
#
# 282:78=3, reszty 48
# 78:48= 1 reszta 30
# 48/30= 1 reszty 18
# 30:18 =1 reszty 12
# 18:12 =1 reszty 6
# 12:6 =2 reszty 0
#
# algorytm hornera - ax^5 + ax^4+ x^n +b = # sposób obliczania wartości wielomianu
#
#
#
# Kodowanie Huffmana
#
#
# slinia = 5! = 5*4*3*2*1


rekurencja:

def silnia(a):
    if a == 1:
        print(a)
        return 1
    else:
        print(a)
        return silnia(a-1)*a

