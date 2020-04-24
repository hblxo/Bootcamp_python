from FileLoader import FileLoader
from ProportionBySport import proportionBySport


fl = FileLoader()
df = fl.load("../resources/athlete_events.csv")
print(proportionBySport(df, 2004, 'Tennis', 'F'))
