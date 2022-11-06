def add_columns_full_time_result(df, team):  
    df.loc[(df.HomeTeam == team) & (df.FTR == "H") , team + ' ' + 'won the match']= 1
    df.loc[(df.AwayTeam == team) & (df.FTR == "A") , team + ' ' + 'won the match']= 1
    df.loc[(df.HomeTeam != team) & (df.FTR == "H") , team + ' ' + 'lost the match']= 1
    df.loc[(df.AwayTeam != team) & (df.FTR == "A") , team + ' ' + 'lost the match']= 1
    df.loc[df.FTR == "D" , 'The match ended with draw result']= 1
    df = df.fillna(0)
    df = df.drop(["Season", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR"], axis=1)
    #df = df.loc[:, (df != 0).any(axis=0)]
    return df

