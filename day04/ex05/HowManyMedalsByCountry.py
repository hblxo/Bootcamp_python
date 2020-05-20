import pandas as pd


def howManyMedalsByCountry(df, country):
    df_filter = df[df.Team == country]
    new_dict = {}
    df_filter = df_filter.dropna()
    df_filter = df_filter.drop_duplicates('Event')
    years = set()
    for year in df_filter['Year']:
        if year not in years:
            years.add(year)
            # yearmin = df_filter.Year.min()
            gold = len(df_filter[(df_filter.Year == year)
                                 & (df_filter.Medal == 'Gold')])
            silver = len(df_filter[(df_filter.Year == year)
                                   & (df_filter.Medal == 'Silver')])
            bronze = len(df_filter[(df_filter.Year == year)
                                   & (df_filter.Medal == 'Bronze')])
            new_dict.update({year: {'G': gold, 'S': silver, 'B': bronze}})
            df_filter = df_filter[df_filter.Year != year]
    return new_dict
