class Rakieta():
    def __init__(self, position=(0, 0)):
        self.position = position

    def move(self, coordinates):
        dx = coordinates[0]
        dy = coordinates[1]
        self.position = (self.position[0] + dx, self.position[1] + dy)
