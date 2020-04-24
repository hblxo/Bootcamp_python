import pandas as pd


def howManyMedals(df, name):
    new_dict = {}
    df_filter = df[(df.Name == name)]
    df_filter = df_filter.dropna()
    while not (df_filter.empty):
        yearmin = df_filter.Year.min()
        gold = len(df_filter[(df_filter.Year == yearmin)
                             & (df_filter.Medal == 'Gold')])
        silver = len(df_filter[(df_filter.Year == yearmin)
                               & (df_filter.Medal == 'Silver')])
        bronze = len(df_filter[(df_filter.Year == yearmin)
                               & (df_filter.Medal == 'Bronze')])
        new_dict.update({yearmin: {'G': gold, 'S': silver, 'B': bronze}})
        df_filter = df_filter[df_filter.Year != yearmin]
    return new_dict
