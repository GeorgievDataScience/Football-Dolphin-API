def add_columns_team_won_first_half(df, team):
    df.loc[(df["HomeTeam"] == team) & (df["HTR"] == "H") & (df["FTR"] == "H") , team + ' ' + 'won the first half time and the match']= 1
    df.loc[(df["AwayTeam"] == team) & (df["HTR"] == "A") & (df["FTR"] == "A") , team + ' ' + 'won the first half time and the match']= 1
    df.loc[(df["HomeTeam"] == team) & (df["HTR"] == "H") & (df["FTR"] == "D") , team + ' ' + 'won the first half time and the match ended with draw result']= 1
    df.loc[(df["AwayTeam"] == team) & (df["HTR"] == "A") & (df["FTR"] == "D") , team + ' ' + 'won the first half time and the match ended with draw result']= 1
    df.loc[(df["HomeTeam"] == team) & (df["HTR"] == "H") & (df["FTR"] == "A") , team + ' ' + 'won the first half time and lost the match']= 1
    df.loc[(df["AwayTeam"] == team) & (df["HTR"] == "A") & (df["FTR"] == "H") , team + ' ' + 'won the first half time and lost the match']= 1
    return df

def add_columns_team_lost_first_half(df, team):
    df.loc[(df["HomeTeam"] != team) & (df["HTR"] == "H") & (df["FTR"] == "H") , team + ' ' + 'lost the first half time and the match']= 1
    df.loc[(df["AwayTeam"] != team) & (df["HTR"] == "A") & (df["FTR"] == "A") , team + ' ' + 'lost the first half time and the match']= 1
    df.loc[(df["HomeTeam"] != team) & (df["HTR"] == "H") & (df["FTR"] == "D") , team + ' ' + 'lost the first half time and the match ended with draw result']= 1
    df.loc[(df["AwayTeam"] != team) & (df["HTR"] == "A") & (df["FTR"] == "D") , team + ' ' + 'lost the first half time and the match ended with draw result']= 1
    df.loc[(df["HomeTeam"] != team) & (df["HTR"] == "H") & (df["FTR"] == "A") , team + ' ' + 'lost the first half time and won the match']= 1
    df.loc[(df["AwayTeam"] != team) & (df["HTR"] == "A") & (df["FTR"] == "H") , team + ' ' + 'lost the first half time and won the match']= 1
    return df


def add_columns_draw_match_first_half(df, team):
    df.loc[(df["HTR"] == "D") & (df["FTR"] == "D") ,'First half time ended with draw result and the match ended with draw result']= 1
    df.loc[(df["HomeTeam"] == team) & (df["HTR"] == "D") & (df["FTR"] == "H") ,'First half time ended with draw result and' + ' ' + team + ' ' + 'won the match']= 1
    df.loc[(df["AwayTeam"] == team) & (df["HTR"] == "D") & (df["FTR"] == "A") ,'First half time ended with draw result and' + ' ' + team + ' ' + 'won the match']= 1
    df.loc[(df["HomeTeam"] == team) & (df["HTR"] == "D") & (df["FTR"] == "H") ,'First half time ended with draw result and' + ' ' + team + ' ' + 'lost the match']= 1
    df.loc[(df["AwayTeam"] == team) & (df["HTR"] == "D") & (df["FTR"] == "A") ,'First half time ended with draw result and' + ' ' + team + ' ' + 'lost the match']= 1
    return df

def add_columns_result_first_half_and_the_match(df, team):
    df = add_columns_team_won_first_half(df, team)
    df = add_columns_team_lost_first_half(df, team)
    df = add_columns_draw_match_first_half(df, team)
    df = df.fillna(0)
    df = df.drop(["Season", "HomeTeam", "AwayTeam", "FTR", "HTR"], axis=1)
    #df = df.loc[:, (df != 0).any(axis=0)]
    return df







