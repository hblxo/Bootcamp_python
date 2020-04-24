from FileLoader import FileLoader
import pandas as pd


def youngestFellah(df, year):
    '''The function returns a dictionary containing the age of the youngest woman and manwho took part in the Olympics on that year. The name of the dictionary’s keys is up to you, but it must beself-explanatory.'''
    df_fil = df[df.Year == year]
    df_fil_f = df_fil[df_fil.Sex == 'F']
    df_fil_m = df_fil[df_fil.Sex == 'M']
    new_dict = {}
    new_dict.update({'f': df_fil_f.Age.min()})
    new_dict.update({'m': df_fil_m.Age.min()})
    return(new_dict)
