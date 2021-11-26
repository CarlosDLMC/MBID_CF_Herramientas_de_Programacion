import numpy as np

class Cuadrado():
    def __init__(self, diagonal):
        self._diagonal = diagonal

    @property
    def diagonal(self):
        print("___in the getter___")
        return self._diagonal

    @diagonal.setter
    def diagonal(self, diagonal):
        print("___in the setter___")
        self._diagonal = diagonal

    @diagonal.deleter
    def diagonal(self):
        print("___in the deleter___")
        del self._diagonal

    def get_side(self):
        return self._diagonal / np.sqrt(2)

sq = Cuadrado(12)
print(sq.get_side())
