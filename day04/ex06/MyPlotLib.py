import pandas as pd
import matplotlib.pyplot as plt
from scipy import misc


class MyPlotLib(object):
    def __init__(self):
        pass

    def histogram(self, data, *features):
        data[list(features)].hist()
        plt.show()

    def density(self, data, *features):
        data[list(features)].plot.density()
        plt.show()

    def pair_plot(self, data, features):
        pass
