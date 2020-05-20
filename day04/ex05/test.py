from FileLoader import FileLoader
from HowManyMedalsByCountry import howManyMedalsByCountry


fl = FileLoader()
df = fl.load("../resources/athlete_events.csv")
print(howManyMedalsByCountry(df, 'France'))
