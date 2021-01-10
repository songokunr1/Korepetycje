import math
from random import randint


class Dyski:
    r = 0.5
    odleglosc = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.x_range = (x - self.r, x + self.r)
        self.y_range = (y - self.r, y + self.r)

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def kolizja(self, drugi_dysk):
        self.odleglosc = math.sqrt((self.x - drugi_dysk.x) ** 2 +
                                   (self.y - drugi_dysk.y) ** 2)
        if self.odleglosc < drugi_dysk.r + self.r:
            return True
        else:
            return False

    def przesunięcie(self, wektor):
        self.x += wektor[0]
        self.y += wektor[1]
        if self.x > 15:
            self.x = -15
        if self.y > 15:
            self.y = -15




def losowanie_wspolrzednych(a=-15, b=15):
    x = randint(a, b)
    y = randint(a, b)
    return [int(x), int(y)]

dyski_początkowe = []
dyski_końcowe = []

x_y = losowanie_wspolrzednych()
print(x_y)
dysk0 = Dyski(x_y[0], x_y[1])
dyski_początkowe.append(dysk0)
dyski_końcowe.append(dysk0)
dysk1 = Dyski(1, 2)
dysk2 = Dyski(1, 0)

# dysk1.kolizja(dysk0)

for i in range(1, 100):
    x_y = losowanie_wspolrzednych()
    dysk_tmp = Dyski(x_y[0], x_y[1])
    dyski_początkowe.append(dysk_tmp)
    i = 0
    while i < len(dyski_końcowe):
        if dyski_końcowe[i].kolizja(dysk_tmp):
            x = [randint(0, 1), 0]
            dysk_tmp.przesunięcie(x)
            i = 0
        if dyski_końcowe[i].kolizja(dysk_tmp):
            y = [0, randint(0, 1)]
            dysk_tmp.przesunięcie(y)
            i = 0
        i += 1
    dyski_końcowe.append(dysk_tmp)

for x in dyski_końcowe:
    print(x)

