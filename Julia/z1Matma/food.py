class Food(object):
    def __init__(self):
        self.consumed = False

    def consume(self):
        self.consumed = True


class Fruit(Food):
    def __init__(self):
        super(Fruit, self).__init__()
        self.been_cut = False

    def cut(self, ostry):
        if ostry == True:
            return True
        else:
            return 'Niestety nie udalo sie tym razem'
        # print("cut the fruit")
        # self.been_cut = True

jablko = Fruit()
jablko.cut(ostry=True)   #  'przeciete'
jablko.cut(ostry=False)  #  'Niestety nie udalo sie'

class Consumer(object):
    def __init__(self):
        self.apple = Fruit()
        self.banana = Fruit()

    def consume_food(self):
        food = self.pick_food()
        food.cut()
        print("consuming the food")
        food.consume()

    def pick_food(self):
        return self.apple