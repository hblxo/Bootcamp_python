import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


class ImageProcessor():
    def __init__(self):
        self.img = None

    def load(self, path):
        self.img = plt.imread(path)
        print('Loading image of dimensions {} x {}'.format(
            self.img.shape[0], self.img.shape[1]))
        return(self.img)

    def display(self, array):
        # print(np.array(array))
        plt.imshow(array)
        plt.show()
