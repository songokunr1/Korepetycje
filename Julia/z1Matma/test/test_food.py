import unittest
from Julia.z1Matma.food import Consumer, Food, Fruit

class TestConsumer(unittest.TestCase):


    def test_czy_noz_tnie(self):
        jablko = Fruit()
        tnie = jablko.cut(ostry=True)  # 'przeciete'
        self.assertEqual(tnie, True)

    def test_czy_noz_nie_tnie(self):
        jablko = Fruit()
        tnie = jablko.cut(ostry=False)
        self.assertEqual(tnie, 'Niestety nie udalo sie')

    # def test_consume_food_consumes_the_apple(self):
    #     c = Consumer()
    #     c.consume_food()
    #     self.assertTrue(c.apple.consumed,
    #                     "Expected apple to be consumed")
    #
    # def test_consume_food_cuts_the_food(self):
    #     c = Consumer()
    #     c.consume_food()
    #     self.assertTrue(c.apple.been_cut,
    #                     "Expected apple to be cut")

    # def test_pick_food_always_selects_the_apple(self):
    #     c = food.Consumer()
    #     food = c.pick_food()
    #     self.assertEquals(c.apple, food,
    #                       "Expected apple to have been picked")


if __name__ == '__main__':
    unittest.main()