import pandas as pd
from database import data
import json

import headtoheadstatistics.totalnumberofmatches as tnm

def database_filter(first_team, second_team, type_of_statistics):
    
    def filtering_rows_by_two_selected_teams(first_team, second_team, selected_columns):
        df = data.df[selected_columns]
        df = df.loc[((df["HomeTeam"] == first_team) & (df["AwayTeam"] == second_team)) | 
                    ((df["HomeTeam"] == second_team) & (df["AwayTeam"] == first_team))]
        return df
    
    def selecting_columns_from_database_by_type_of_statistics(type_of_statistics):
        if type_of_statistics == "full time result":
            selected_columns = ["Season", "HomeTeam", "AwayTeam", "FTHG", "FTAG", 
                                  "FTR", "Total number of played matches"]
        
        if type_of_statistics == "home vs away full time result":
            selected_columns = ["Season", "HomeTeam", "AwayTeam", "FTR", 
                                  "Total number of played matches"]
        
        if type_of_statistics == "result first half and the match":
            selected_columns = ["Season", "HomeTeam", "AwayTeam", 
                                  "FTR", "HTR", "Total number of played matches"]
        
        if type_of_statistics == "exact number of goals in the match":
            selected_columns = ["Season", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR", 
                                "Total number of played matches"]
        
        if type_of_statistics == "goals over":
            selected_columns = ["Season", "HomeTeam", "AwayTeam", "FTHG", "FTAG", 
                                "FTR", "Total number of played matches"]
        
        if type_of_statistics == "goals under":
            selected_columns = ["Season", "HomeTeam", "AwayTeam", "FTHG", "FTAG", 
                                "FTR", "Total number of played matches"]
        return selected_columns
    
    df = filtering_rows_by_two_selected_teams(
        first_team, 
        second_team, 
        selecting_columns_from_database_by_type_of_statistics(type_of_statistics))
    return df


def zero_played_matches(first_team, second_team):
    message = {
        "message" : first_team + " vs " + second_team + " 0 played matches in period (" + data.df["Season"].iloc[0] + " - " + data.df["Season"].iloc[-1] + ")"   
    }
    return message


def selecting_type_of_statistics(
        df, first_team, second_team, type_of_statistics):
    
    if type_of_statistics == "full time result":
        df = tnm.full_time_result.add_columns_full_time_result(
            df, first_team, second_team)
        
    if type_of_statistics == "home vs away full time result":
        df = tnm.home_vs_away_full_time_result.add_columns_home_vs_away_full_time_result(
            df, first_team, second_team)
    
    if type_of_statistics == "result first half and the match":
        df = tnm.result_first_half_and_the_match.add_columns_result_first_half_and_the_match(
            df, first_team, second_team)
    
    if type_of_statistics == "exact number of goals in the match":
        df = tnm.exact_number_of_goals_in_the_match.add_columns_exact_number_of_goals_in_the_match(df)
         
    if type_of_statistics == "goals over":
        df = tnm.goals_over_under_in_the_match.add_columns_goals_over_in_the_match(df)
    
    if type_of_statistics == "goals under":
        df = tnm.goals_over_under_in_the_match.add_columns_goals_under_in_the_match(df)
        
    return df 

   
def final_step(df, first_team, second_team):
    def sum_values_in_df_by_columns(df):
        df = pd.DataFrame(df.sum()).T
        return df

    def add_column_time_period(df, first_team, second_team):
        df.insert(0, "Period", "From season " + data.df["Season"].iloc[0] + " to "+ data.df["Season"].iloc[-1] + " in English Premier League")
        df.insert(0, "H2H", first_team + " vs " + second_team)
        #df["H2H"] = firstteam + " vs " + secondteam
        return df

    def change_df_to_json_table(df):
        df = df.to_json(orient="records")
        df_parsed = json.loads(df)
        return df_parsed
    
    df = sum_values_in_df_by_columns(df)
    df = add_column_time_period(df, first_team, second_team)
    df = change_df_to_json_table(df)
    return df


def main_function_for_data_analysis(
        type_of_statistics, first_team, second_team):
    
    df = database_filter(first_team, second_team, type_of_statistics)       
    if df.empty:
        message = zero_played_matches(first_team, second_team)
        return message
    else:
         df = selecting_type_of_statistics(
             df, first_team, second_team, type_of_statistics)
         
         df = final_step(df, first_team, second_team)
         return df

