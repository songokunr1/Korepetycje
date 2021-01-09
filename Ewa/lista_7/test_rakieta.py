from Ewa.lista_7.rakieta import Rakieta


def test_rover_is_created():
    position = (0, 0)
    created_object = Rakieta(position)
    assert isinstance(created_object, Rakieta)


def test_move():
    """ x and y move"""
    created_object = Rakieta()
    created_object.move((1, 1))
    assert created_object.position == (1, 1)


def test_get_position():
    print()
    # assert rakieta_instance.position == (x_coordinate, y_coordinate)


def test_get_distance():
    pass
