import pandas as pd


class SpatioTemporalData():
    df = None

    def __init__(self, df):
        self.df = df

    def when(self, location):
        date = []
        seen = set()
        filter_df = self.df[self.df.City == location]
        for year in filter_df['Year']:
            if year not in seen:
                seen.add(year)
                date.append(year)
        return date

    def where(self, date):
        filter_df = self.df[self.df.Year == date]
        seen = set()
        location = []
        for city in filter_df['City']:
            if city not in seen:
                seen.add(city)
                location.append(city)
        return location
