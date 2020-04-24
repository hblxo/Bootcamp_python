import pandas as pd


def proportionBySport(df, year, sport, gender):
    df_filter = df[df.Sex == gender]
    gender_count = df_filter.shape[0]
    df_filter_sport = df_filter[df_filter.Sport == sport]
    return(df_filter_sport.shape[0] / gender_count)
