def add_columns_all_scores_full_time(df):
    df.loc[(df.FTHG == 0) & (df.FTAG == 0) ,'0-0']= 1
    df.loc[(df.FTHG == 1) & (df.FTAG == 0) ,'1-0']= 1
    df.loc[(df.FTHG == 2) & (df.FTAG == 0) ,'2-0']= 1
    df.loc[(df.FTHG == 3) & (df.FTAG == 0) ,'3-0']= 1
    df.loc[(df.FTHG == 4) & (df.FTAG == 0) ,'4-0']= 1
    df.loc[(df.FTHG == 5) & (df.FTAG == 0) ,'5-0']= 1
    df.loc[(df.FTHG == 6) & (df.FTAG == 0) ,'6-0']= 1
    df.loc[(df.FTHG == 7) & (df.FTAG == 0) ,'7-0']= 1
    df.loc[(df.FTHG == 0) & (df.FTAG == 1) ,'0-1']= 1
    df.loc[(df.FTHG == 1) & (df.FTAG == 1) ,'1-1']= 1
    df.loc[(df.FTHG == 2) & (df.FTAG == 1) ,'2-1']= 1
    df.loc[(df.FTHG == 3) & (df.FTAG == 1) ,'3-1']= 1
    df.loc[(df.FTHG == 4) & (df.FTAG == 1) ,'4-1']= 1
    df.loc[(df.FTHG == 5) & (df.FTAG == 1) ,'5-1']= 1
    df.loc[(df.FTHG == 6) & (df.FTAG == 1) ,'6-1']= 1
    df.loc[(df.FTHG == 7) & (df.FTAG == 1) ,'7-1']= 1
    df.loc[(df.FTHG == 0) & (df.FTAG == 2) ,'0-2']= 1
    df.loc[(df.FTHG == 1) & (df.FTAG == 2) ,'1-2']= 1
    df.loc[(df.FTHG == 2) & (df.FTAG == 2) ,'2-2']= 1
    df.loc[(df.FTHG == 3) & (df.FTAG == 2) ,'3-2']= 1
    df.loc[(df.FTHG == 4) & (df.FTAG == 2) ,'4-2']= 1
    df.loc[(df.FTHG == 5) & (df.FTAG == 2) ,'5-2']= 1
    df.loc[(df.FTHG == 6) & (df.FTAG == 2) ,'6-2']= 1
    df.loc[(df.FTHG == 7) & (df.FTAG == 2) ,'7-2']= 1
    df.loc[(df.FTHG == 0) & (df.FTAG == 3) ,'0-3']= 1
    df.loc[(df.FTHG == 1) & (df.FTAG == 3) ,'1-3']= 1
    df.loc[(df.FTHG == 2) & (df.FTAG == 3) ,'2-3']= 1
    df.loc[(df.FTHG == 3) & (df.FTAG == 3) ,'3-3']= 1
    df.loc[(df.FTHG == 4) & (df.FTAG == 3) ,'4-3']= 1
    df.loc[(df.FTHG == 5) & (df.FTAG == 3) ,'5-3']= 1
    df.loc[(df.FTHG == 6) & (df.FTAG == 3) ,'6-3']= 1
    df.loc[(df.FTHG == 7) & (df.FTAG == 3) ,'7-3']= 1
    df.loc[(df.FTHG == 0) & (df.FTAG == 4) ,'0-4']= 1
    df.loc[(df.FTHG == 1) & (df.FTAG == 4) ,'1-4']= 1
    df.loc[(df.FTHG == 2) & (df.FTAG == 4) ,'2-4']= 1
    df.loc[(df.FTHG == 3) & (df.FTAG == 4) ,'3-4']= 1
    df.loc[(df.FTHG == 4) & (df.FTAG == 4) ,'4-4']= 1
    df.loc[(df.FTHG == 5) & (df.FTAG == 4) ,'5-4']= 1
    df.loc[(df.FTHG == 6) & (df.FTAG == 4) ,'6-4']= 1
    df.loc[(df.FTHG == 7) & (df.FTAG == 4) ,'7-4']= 1
    df.loc[(df.FTHG == 0) & (df.FTAG == 5) ,'0-5']= 1
    df.loc[(df.FTHG == 1) & (df.FTAG == 5) ,'1-5']= 1
    df.loc[(df.FTHG == 2) & (df.FTAG == 5) ,'2-5']= 1
    df.loc[(df.FTHG == 3) & (df.FTAG == 5) ,'3-5']= 1
    df.loc[(df.FTHG == 4) & (df.FTAG == 5) ,'4-5']= 1
    df.loc[(df.FTHG == 5) & (df.FTAG == 5) ,'5-5']= 1
    df.loc[(df.FTHG == 6) & (df.FTAG == 5) ,'6-5']= 1
    df.loc[(df.FTHG == 7) & (df.FTAG == 5) ,'7-5']= 1
    df.loc[(df.FTHG == 0) & (df.FTAG == 6) ,'0-6']= 1
    df.loc[(df.FTHG == 1) & (df.FTAG == 6) ,'1-6']= 1
    df.loc[(df.FTHG == 2) & (df.FTAG == 6) ,'2-6']= 1
    df.loc[(df.FTHG == 3) & (df.FTAG == 6) ,'3-6']= 1
    df.loc[(df.FTHG == 4) & (df.FTAG == 6) ,'4-6']= 1
    df.loc[(df.FTHG == 5) & (df.FTAG == 6) ,'5-6']= 1
    df.loc[(df.FTHG == 6) & (df.FTAG == 6) ,'6-6']= 1
    df.loc[(df.FTHG == 7) & (df.FTAG == 6) ,'7-6']= 1
    df.loc[(df.FTHG == 0) & (df.FTAG == 7) ,'0-7']= 1
    df.loc[(df.FTHG == 1) & (df.FTAG == 7) ,'1-7']= 1
    df.loc[(df.FTHG == 2) & (df.FTAG == 7) ,'2-7']= 1
    df.loc[(df.FTHG == 3) & (df.FTAG == 7) ,'3-7']= 1
    df.loc[(df.FTHG == 4) & (df.FTAG == 7) ,'4-7']= 1
    df.loc[(df.FTHG == 5) & (df.FTAG == 7) ,'5-7']= 1
    df.loc[(df.FTHG == 6) & (df.FTAG == 7) ,'6-7']= 1
    df.loc[(df.FTHG == 7) & (df.FTAG == 7) ,'7-7']= 1
    df = df.fillna(0)
    df = df.drop(['FTHG', 'FTAG', 'Season'], axis=1)
    df = df.loc[:, (df != 0).any(axis=0)]
    return df



