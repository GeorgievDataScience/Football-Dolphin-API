def add_columns_exact_number_of_goals_in_th_match(df):   
    df["Total number of goals for all played matches"] = df["FTHG"] + df["FTAG"] 
    df.loc[(df["Total number of goals for all played matches"] == 0) ,'Matches with 0 scored goals']= 1
    df.loc[(df["Total number of goals for all played matches"] == 1) ,'Matches with 1 scored goals']= 1
    df.loc[(df["Total number of goals for all played matches"] == 2) ,'Matches with 2 scored goals']= 1
    df.loc[(df["Total number of goals for all played matches"] == 3) ,'Matches with 3 scored goals']= 1
    df.loc[(df["Total number of goals for all played matches"] == 4) ,'Matches with 4 scored goals']= 1
    df.loc[(df["Total number of goals for all played matches"] == 5) ,'Matches with 5 scored goals']= 1
    df.loc[(df["Total number of goals for all played matches"] == 6) ,'Matches with 6 scored goals']= 1
    df.loc[(df["Total number of goals for all played matches"] == 7) ,'Matches with 7 scored goals']= 1
    df.loc[(df["Total number of goals for all played matches"] == 8) ,'Matches with 8 scored goals']= 1
    df.loc[(df["Total number of goals for all played matches"] == 9) ,'Matches with 9 scored goals']= 1
    df.loc[(df["Total number of goals for all played matches"] == 10) ,'Matches with 10 scored goals']= 1
    df.loc[(df["Total number of goals for all played matches"] == 11) ,'Matches with 11 scored goals']= 1
    df.loc[(df["Total number of goals for all played matches"] == 12) ,'Matches with 12 scored goals']= 1
    df = df.fillna(0)
    df = df.drop(["Season", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR", "Total number of goals for all played matches"], axis=1)
    #df = df.loc[:, (df != 0).any(axis=0)]
    return df

