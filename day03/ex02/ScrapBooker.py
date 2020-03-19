import numpy as np


class ScrapBooker():
    def __init__(self):
        pass

    def crop(self, array, dimensions, position=(0, 0)):
        try:
            assert array.shape > dimensions
        except:
            print("Dimensions can't be larger than array shape")
        train = array[position[0]:dimensions[0], position[1]:dimensions[1]]
        return train

    def thin(self, array, n, axis):
        axis = 1 - axis
        ret = []
        for i in range(1, array.shape[axis]):
            if not i % n:
                ret.append(i - 1)
        res = np.delete(array, ret, axis)
        return res

    def juxtapose(self, array, n, axis):
        return np.concatenate([array] * n, axis=axis)

    def mosaic(self, array, dimensions):
        return np.tile(array, dimensions)
