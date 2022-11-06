def add_columns_full_time_result(df, first_team, second_team):  
    df.loc[(df.HomeTeam == first_team) & (df.FTR == "H") , first_team + ' won the match']= 1
    df.loc[(df.AwayTeam == first_team) & (df.FTR == "A") , first_team + ' won the match']= 1
    df.loc[(df.HomeTeam == second_team) & (df.FTR == "H") , second_team + ' won the match']= 1
    df.loc[(df.AwayTeam == second_team) & (df.FTR == "A") , second_team + ' won the match']= 1
    df.loc[df.FTR == "D" , 'The match ended with draw result']= 1
    df = df.fillna(0)
    df = df.drop(["Season", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR"], axis=1)
    #df = df.loc[:, (df != 0).any(axis=0)]
    return df


