import pandas as pd


class FileLoader():
    def __init__(self):
        pass

    def load(self, path):
        '''he argument of this method is the file path of the dataset to load. It must display amessage specifying the dimensions of the dataset (e.g. 340 x 500). The method returns the dataset loaded as a pandas.DataFrame.'''
        df = pd.read_csv(path)
        print("Loading dataset of dimensions ",
              df.shape[0], " x ", df.shape[1])
        return df

    def display(self, df, n):
        '''Takes a pandas.DataFrame and an integer as arguments. This method displays the first n rows of the dataset if n is positive, or the last n rows if n is negative'''
        if n < 0:
            print(df[n::])
        else:
            print(df[:n:])
