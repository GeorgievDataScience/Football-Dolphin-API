def add_columns_home_vs_away_full_time_result(df):
    df.loc[(df.FTR == 'H') ,'Home team won the match']= 1
    df.loc[(df.FTR == 'A') ,'Away team won the match']= 1
    df.loc[(df.FTR == 'D') ,'Matches with draw result']= 1
    #df = df.fillna(0)
    df = df.drop(["FTR", "Season"], axis=1)
    return df

