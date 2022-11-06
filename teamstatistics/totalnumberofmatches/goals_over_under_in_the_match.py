def add_columns_goals_under(df):   
    df["Goals per Match"] = df["FTHG"] + df["FTAG"] 
    df.loc[df["Goals per Match"] <= 0.5, "Matches with goals under 0.5"] = 1
    df.loc[df["Goals per Match"] <= 1.5, "Matches with goals under 1.5"] = 1
    df.loc[df["Goals per Match"] <= 2.5, "Matches with goals under 2.5"] = 1
    df.loc[df["Goals per Match"] <= 3.5, "Matches with goals under 3.5"] = 1
    df.loc[df["Goals per Match"] <= 4.5, "Matches with goals under 4.5"] = 1
    df.loc[df["Goals per Match"] <= 5.5, "Matches with goals under 5.5"] = 1
    df.loc[df["Goals per Match"] <= 6.5, "Matches with goals under 6.5"] = 1
    df.loc[df["Goals per Match"] <= 7.5, "Matches with goals under 7.5"] = 1
    df.loc[df["Goals per Match"] <= 8.5, "Matches with goals under 8.5"] = 1
    df.loc[df["Goals per Match"] <= 9.5, "Matches with goals under 9.5"] = 1
    df = df.fillna(0)
    df = df.drop(["Season", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR", "Goals per Match"], axis=1)
    #df = df.loc[:, (df != 0).any(axis=0)]
    return df# -*- coding: utf-8 -*-

def add_columns_goals_over(df):
    df["Goals per Match"] = df["FTHG"] + df["FTAG"] 
    df.loc[df["Goals per Match"] >= 0.5, "Matches with goals over 0.5"] = 1
    df.loc[df["Goals per Match"] >= 1.5, "Matches with goals over 1.5"] = 1
    df.loc[df["Goals per Match"] >= 2.5, "Matches with goals over 2.5"] = 1
    df.loc[df["Goals per Match"] >= 3.5, "Matches with goals over 3.5"] = 1
    df.loc[df["Goals per Match"] >= 4.5, "Matches with goals over 4.5"] = 1
    df.loc[df["Goals per Match"] >= 5.5, "Matches with goals over 5.5"] = 1
    df.loc[df["Goals per Match"] >= 6.5, "Matches with goals over 6.5"] = 1
    df.loc[df["Goals per Match"] >= 7.5, "Matches with goals over 7.5"] = 1
    df.loc[df["Goals per Match"] >= 8.5, "Matches with goals over 8.5"] = 1
    df.loc[df["Goals per Match"] >= 9.5, "Matches with goals over 9.5"] = 1
    df = df.fillna(0)
    df = df.drop(["Season", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR", "Goals per Match"], axis=1)
    #df = df.loc[:, (df != 0).any(axis=0)]
    return df




