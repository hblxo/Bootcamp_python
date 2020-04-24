import numpy as np


class ColorFilter():
    def __init__(self):
        pass

    def invert(self, array):
        return 1 - array

    def to_blue(self, array):
        # creer une nouvelle matrice remplie de 0 de la meme shape que l'array
        new = np.zeros(array.shape)
        # remplit les channels rouge (0) et vert (1) de zeros
        # new[:, :, 0] = np.zeros(array[:, :, 0].shape)
        # new[:, :, 1] = np.zeros(array[:, :, 1].shape)
        # copie le channel bleu (2) de array vers new
        new[:, :, 2] = array[:, :, 2]
        return new

    def to_green(self, array):
        return array * [0, 1, 0]

    def to_red(self, array):
        return array - self.to_blue(array) - self.to_green(array)

    def celluloid(self, array, tresh=4):
        # pas compris
        new = np.array(array)
        hold = np.linspace(0.0, 1.0, num=tresh, endpoint=False)[::-1]
        for i in hold:
            indexes = array >= i
            array[indexes] = -1
            new[indexes] = i
        return new

    def to_grayscale(self, array, filter):
        return array
