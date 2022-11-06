def add_columns_first_team_result_first_half(df, first_team, second_team):
    df.loc[(df["HomeTeam"] == first_team) & (df["HTR"] == "H") & (df["FTR"] == "H") , first_team + ' ' + 'won the first half time and the match']= 1
    df.loc[(df["AwayTeam"] == first_team) & (df["HTR"] == "A") & (df["FTR"] == "A") , first_team + ' ' + 'won the first half time and the match']= 1
    df.loc[(df["HomeTeam"] == first_team) & (df["HTR"] == "H") & (df["FTR"] == "D") , first_team + ' ' + 'won the first half time and the match ended with draw result']= 1
    df.loc[(df["AwayTeam"] == first_team) & (df["HTR"] == "A") & (df["FTR"] == "D") , first_team + ' ' + 'won the first half time and the match ended with draw result']= 1
    df.loc[(df["HomeTeam"] == first_team) & (df["HTR"] == "H") & (df["FTR"] == "A") , first_team + ' ' + 'won the first half time and' + ' ' + second_team + ' ' + 'won the match']= 1
    df.loc[(df["AwayTeam"] == first_team) & (df["HTR"] == "A") & (df["FTR"] == "H") , first_team + ' ' + 'won the first half time and' + ' ' + second_team + ' ' + 'won the match']= 1
    return df

def add_columns_second_team_result_first_half(df, first_team, second_team):
    df.loc[(df["HomeTeam"] == second_team) & (df["HTR"] == "H") & (df["FTR"] == "H") , second_team + ' ' + 'won the first half time and the match']= 1
    df.loc[(df["AwayTeam"] == second_team) & (df["HTR"] == "A") & (df["FTR"] == "A") , second_team + ' ' + 'won the first half time and the match']= 1
    df.loc[(df["HomeTeam"] == second_team) & (df["HTR"] == "H") & (df["FTR"] == "D") , second_team + ' ' + 'won the first half time and the match ended with draw result']= 1
    df.loc[(df["AwayTeam"] == second_team) & (df["HTR"] == "A") & (df["FTR"] == "D") , second_team + ' ' + 'won the first half time and the match ended with draw result']= 1
    df.loc[(df["HomeTeam"] == second_team) & (df["HTR"] == "H") & (df["FTR"] == "A") , second_team + ' ' + 'won the first half time and' + ' ' + first_team + ' ' + 'won the match']= 1
    df.loc[(df["AwayTeam"] == second_team) & (df["HTR"] == "A") & (df["FTR"] == "H") , second_team + ' ' + 'won the first half time and' + ' ' + first_team + ' ' + 'won the match']= 1
    return df

def add_columns_draw_match_result_first_half(df, first_team, second_team):
    df.loc[(df["HTR"] == "D") & (df["FTR"] == "D") ,'First half time ended with draw result and and the match ended with draw result']= 1
    df.loc[(df["HomeTeam"] == first_team) & (df["HTR"] == "D") & (df["FTR"] == "H") ,'First half time ended with draw result and' + ' ' + first_team + ' ' + 'won the match']= 1
    df.loc[(df["AwayTeam"] == first_team) & (df["HTR"] == "D") & (df["FTR"] == "A") ,'First half time ended with draw result and' + ' ' + first_team + ' ' + 'won the match']= 1
    df.loc[(df["HomeTeam"] == second_team) & (df["HTR"] == "D") & (df["FTR"] == "H") ,'First half time ended with draw result and' + ' ' + second_team + ' ' + 'won the match']= 1
    df.loc[(df["AwayTeam"] == second_team) & (df["HTR"] == "D") & (df["FTR"] == "A") ,'First half time ended with draw result and' + ' ' + second_team + ' ' + 'won the match']= 1
    return df

def add_columns_result_first_half_and_the_match(df, first_team, second_team):
    df = add_columns_first_team_result_first_half(df, first_team, second_team)
    df = add_columns_second_team_result_first_half(df, first_team, second_team)
    df = add_columns_draw_match_result_first_half(df, first_team, second_team)
    df = df.fillna(0)
    df = df.drop(["Season", "HomeTeam", "AwayTeam", "FTR", "HTR"], axis=1)
    #df = df.loc[:, (df != 0).any(axis=0)]
    return df





