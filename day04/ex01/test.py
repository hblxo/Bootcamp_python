from FileLoader import FileLoader
from YoungestFellah import youngestFellah

fl = FileLoader()
df = fl.load("../resources/athlete_events.csv")
print(youngestFellah(df, 2004))
