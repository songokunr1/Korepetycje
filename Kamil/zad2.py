#0 0, 0 1
#0 1, 0 2
from random import choice
import matplotlib.pyplot as plt


# początek 0,0
# tworzenie ruchu(poczatek) -> koniec
# zapamietywanie ruchu
# rysowanie kolejnego ruchu
# zdjecie

class Point:
    def __init__(self, x=0, y=0):
        self.starting_x_y = (x, y)
        self.ending_x_y = (None, None)


    def set_ending_point(self):
        vektor = [0,0]
        x_or_y = choice([0,1])
        vektor[x_or_y] = choice([-1,1])
        self.ending_x_y = (self.starting_x_y[0] + vektor[0], self.starting_x_y[1] + vektor[1])

    def rysuj(self):
        plt.plot([self.starting_x_y[0], self.ending_x_y[0]], [self.starting_x_y[1], self.ending_x_y[1]])

def create_move():
    pass


class Points:
    poczatek = Point(0,0)
    poczatek.set_ending_point()
    def __init__(self):
        self.points = [self.poczatek]
        self.last_ending_points = self.poczatek.ending_x_y
        for _ in range(100):
            new_point = Point(self.last_ending_points[0], self.last_ending_points[1])
            new_point.set_ending_point()
            self.points.append(new_point)
            self.last_ending_points = new_point.ending_x_y


    def chars(self):
        for moves in range(len(self.points)):
            for move in range(moves):
                self.points[move].rysuj()
            plt.savefig(f'{moves}.png')


a = Points()
a.chars()