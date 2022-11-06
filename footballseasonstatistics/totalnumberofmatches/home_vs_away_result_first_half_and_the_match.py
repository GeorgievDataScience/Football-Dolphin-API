def add_columns_home_team_result_first_half(df):
    df.loc[(df["HTR"] == "H") & (df["FTR"] == "H") , 'The home team won the first half time and the match']= 1
    df.loc[(df["HTR"] == "H") & (df["FTR"] == "D") , 'The home team won the first half time and the match ended with draw result']= 1    
    df.loc[(df["HTR"] == "H") & (df["FTR"] == "A") , 'The home team won the first half time and the away team won the match']= 1 
    return df


def add_columns_away_team_result_first_half(df):
    df.loc[(df["HTR"] == "A") & (df["FTR"] == "A") , 'The away team won the first half time and the match']= 1
    df.loc[(df["HTR"] == "A") & (df["FTR"] == "D") , 'The away team won the first half time and the match ended with draw result']= 1
    df.loc[(df["HTR"] == "A") & (df["FTR"] == "H") , 'The away team won the first half time and the home team won the match']= 1
    return df


def add_columns_draw_match_result_first_half(df):
    df.loc[(df["HTR"] == "D") & (df["FTR"] == "D") ,'First half time ended with draw result and the match ended with draw result']= 1
    df.loc[(df["HTR"] == "D") & (df["FTR"] == "H") ,'First half time ended with draw result and the home team won the match']= 1
    df.loc[(df["HTR"] == "D") & (df["FTR"] == "A") ,'First half time ended with draw result and the away team won the match']= 1
    return df

def add_columns_home_vs_away_result_first_half_and_the_match(df):
    df = add_columns_home_team_result_first_half(df)
    df = add_columns_away_team_result_first_half(df)
    df = add_columns_draw_match_result_first_half(df)
    df = df.fillna(0)
    df = df.drop(["Season", "HomeTeam", "AwayTeam", "FTR", "HTR"], axis=1)
    #df = df.loc[:, (df != 0).any(axis=0)]
    return df



