def add_columns_home_vs_away_full_time_result(df, team):
    df.loc[(df.HomeTeam == team) & (df.FTR == "H") , team + ' ' + 'won as a host']= 1
    df.loc[(df.AwayTeam == team) & (df.FTR == "A") , team + ' ' + 'won as a guest']= 1
    df.loc[(df.HomeTeam == team) & (df.FTR == "D") , team + ' was the home team and the match ended with draw result']= 1
    df.loc[(df.AwayTeam == team) & (df.FTR == "D") , team + ' was the away team and the match ended with draw result']= 1
    df.loc[(df.HomeTeam == team) & (df.FTR == "A") , team + ' ' + 'lost as a host']= 1
    df.loc[(df.AwayTeam == team) & (df.FTR == "H") , team + ' ' + 'lost as a guest']= 1
    df = df.fillna(0)
    df = df.drop(["Season", "HomeTeam", "AwayTeam", "FTR"], axis=1)
    #df = df.loc[:, (df != 0).any(axis=0)]
    return df

