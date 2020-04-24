from FileLoader import FileLoader

fl = FileLoader()
df = fl.load("../resources/athlete_events.csv")
fl.display(df, -5)
fl.display(df, 5)
