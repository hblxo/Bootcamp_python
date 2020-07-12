from FileLoader import FileLoader
from MyPlotLib import MyPlotLib


fl = FileLoader()
df = fl.load("../resources/athlete_events.csv")

mpl = MyPlotLib()
mpl.histogram(df, 'Year', 'Height')
