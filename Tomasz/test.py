global lista_pilek
lista_pilek = []
def nowa_piłka(b):
    # global
    # [{"piłka_x": 1, "piłka_y":2, "piłka_dx": 1, "piłka_dy":2}, [piłka_x, piłka_y, piłka_dx, piłka_dy]]
    global lista_pilek
    # global piłka_x, piłka_y, piłka_dx, piłka_dy
    phi = 5
    # tworzymy slownik, pusty,
    # dopisujemy wartosci
    # dodajemy slownik do listy
    piłka_x = b
    piłka_y = b
    piłka_dx = b
    piłka_dy = b

    a = {}
    a['piłka_x'] = piłka_x
    a['piłka_y'] = piłka_y
    a['piłka_dx'] = piłka_dx
    a['piłka_dy'] = piłka_dy

    lista_pilek.append(a)


nowa_piłka(4)
nowa_piłka(3)
nowa_piłka(2)
lista_pilek[1]['piłka_y'] = 10
print(lista_pilek[1]['piłka_y'])

