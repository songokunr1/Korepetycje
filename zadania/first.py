import numpy as np
def pascal(n=1, trojkat=True):
    if n == 0:
        return [[1]]
    if n == 1:
        return [[1], [1, 1]]
    if n >= 1:
        piramida = [[1], [1, 1]]
        size = 1
        while size < n:
            piramida.append(get_next_level(piramida[-1]))
            size += 1
        if trojkat:
            return piramida
        else:
            return piramida[n]


def pascal_napis(n=3, x='x', y='y'):
    piramida = pascal(n, False)
    napis = ''
    index = 0
    while index <= n:
        if index == 0:
            napis += fr'{x}^{n - index} + '
            index += 1
            continue
        elif index == n:
            napis += fr'{y}^{index}'
            index += 1
            continue
        napis += fr'{piramida[index]}*{x}^{n - index}*{y}^{index} + '
        index += 1
    return napis.replace(f"^1*", "*").replace(f"^1 ", " ")


def piramida_pascala(n=3):
    piramida = pascal(n)
    warstwa = pascal(n, trojkat=False)
    index = 0
    while index <= n:
        nowa_warstwa = np.array(piramida[index]) * warstwa[index]
        piramida[index] = nowa_warstwa.tolist()
        index += 1
    # nowa = [[single] for single in warstwa]
    # nowa_piramida = np.array(piramida) * np.array(nowa)
    return piramida


def piramida_pascal_napis(n=1, x='x', y='y', z='z'):
    piramida = piramida_pascala(n=n)
    napis = ''
    index = 0
    while index <= n:
        if index == 0:
            napis += fr'{x}^{n - index} + '
            index += 1
            continue
        elif index == n:
            napis += fr'{y}^{index}'
            index += 1
            continue
        napis += fr'{piramida[index]}*{x}^{n - index}*{y}^{index}*{z}^{index} + '
        index += 1
    return napis.replace(f"^1*", "*").replace(f"^1 ", " ")


def get_next_level(last_level=[]):
    new_level = []
    index = 0
    while True:
        if last_level[index] == 1:
            new_level.append(1)
        new_level.append(last_level[index] + last_level[index + 1])  #tutaj bedzie ostatni elemet
        if last_level[index + 1] == 1: #wiec tutaj tez musi byc +1
            new_level.append(1)
            break
        index += 1
    return new_level

print(piramida_pascala(4))

print(piramida_pascal_napis(4))
