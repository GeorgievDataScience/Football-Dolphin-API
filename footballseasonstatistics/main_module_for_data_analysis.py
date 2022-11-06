import pandas as pd
from database import data
import json

import footballseasonstatistics.totalnumberofmatches as tnm

def database_filter(season, type_of_statistics):
    
    def filtering_rows_by_season(season, selected_columns):
        df = data.df[selected_columns]
        df = df.loc[df['Season'] == season ]
        return df
    
    def selecting_columns_from_database_by_type_of_statistics(type_of_statistics):
        if type_of_statistics == "all scores":
            selected_columns = ["Season", "FTHG", "FTAG", "Total number of played matches"]
        
        if type_of_statistics == "exact number of goals in the match":
            selected_columns = ["Season", "HomeTeam", "AwayTeam", "FTHG", "FTAG", 
                                "FTR", "Total number of played matches"]
        
        if type_of_statistics == "goals over":
            selected_columns = ["Season", "HomeTeam", "AwayTeam", "FTHG", "FTAG", 
                                "FTR", "Total number of played matches"]
        
        if type_of_statistics == "goals under":
            selected_columns = ["Season", "HomeTeam", "AwayTeam", "FTHG", "FTAG", 
                                "FTR", "Total number of played matches"]
                
        if type_of_statistics == "home vs away full time result":
            selected_columns = ["Season", "FTR", "Total number of played matches"]
        
        if type_of_statistics == "home vs away result first half and the match":
            selected_columns = ["Season", "HomeTeam", "AwayTeam", "FTR", "HTR", 
                                "Total number of played matches"]
        return selected_columns
    
    df = filtering_rows_by_season(
        season, 
        selecting_columns_from_database_by_type_of_statistics(type_of_statistics))
    
    return df



def selecting_type_of_statistics(
        df, season, type_of_statistics):
    
    if type_of_statistics == "all scores":
        df = tnm.all_scores_full_time.add_columns_all_scores_full_time(df)
        
    if type_of_statistics == "exact number of goals in the match":
        df = tnm.exact_number_of_goals_in_the_match.add_columns_exact_number_of_goals_in_th_match(df)
    
    if type_of_statistics == "goals over":
        df = tnm.goals_over_under_in_the_match.add_columns_goals_over_in_the_match(df)
    
    if type_of_statistics == "goals under":
        df = tnm.goals_over_under_in_the_match.add_columns_goals_under_in_the_match(df)
        
    if type_of_statistics == "home vs away full time result":
        df = tnm.home_vs_away_full_time_result.add_columns_home_vs_away_full_time_result(df)
        
    if type_of_statistics == "home vs away result first half and the match":
        df = tnm.home_vs_away_result_first_half_and_the_match.add_columns_home_vs_away_result_first_half_and_the_match(df)
        
    return df 

   
def final_step(df, season):
    def sum_values_in_df_by_columns(df):
        df = pd.DataFrame(df.sum()).T
        return df

    def add_column_time_period(df, season):
        df.insert(0, "Season", season)
        return df

    def change_df_to_json_table(df):
        df = df.to_json(orient="records")
        df_parsed = json.loads(df)
        return df_parsed
    
    df = sum_values_in_df_by_columns(df)
    df = add_column_time_period(df, season)
    df = change_df_to_json_table(df)
    return df


def main_function_for_data_analysis(type_of_statistics, season):    
    df = database_filter(season, type_of_statistics)       
    df = selecting_type_of_statistics(df, season, type_of_statistics)
    df = final_step(df, season)
    return df



