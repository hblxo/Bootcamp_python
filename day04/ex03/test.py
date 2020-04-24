from FileLoader import FileLoader
from HowManyMedals import howManyMedals


fl = FileLoader()
df = fl.load("../resources/athlete_events.csv")
print(howManyMedals(df, 'Kjetil Andr Aamodt'))
