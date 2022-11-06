from fastapi import FastAPI
from enum import Enum

from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import  Request

from database import data

import headtoheadstatistics.main_module_for_data_analysis as hth
import footballseasonstatistics.main_module_for_data_analysis as sn
import teamstatistics.main_module_for_data_analysis as tm



app = FastAPI()



available_types_of_head_to_head_statistics = ["full time result", 
                                              "home vs away full time result", 
                                              "result first half and the match", 
                                              "exact number of goals in the match", 
                                              "goals over", "goals under"]

all_teams = ["Arsenal", "Aston Villa", "Barnsley", "Birmingham", "Blackburn", 
            "Blackpool", "Bolton", "Bournemouth", "Bradford", "Brighton", 
            "Burnley", "Cardiff", "Charlton", "Chelsea", "Coventry", 
            "Crystal Palace", "Derby", "Everton", "Fulham", "Huddersfield",
            "Hull", "Ipswich", "Leeds", "Leicester", "Liverpool", "Man City",
            "Man United", "Middlesbrough", "Newcastle", "Norwich", "Nott'm Forest",
            "Portsmouth", "QPR", "Reading", "Sheffield United", "Sheffield Weds",
            "Southampton", "Stoke", "Sunderland", "Swansea", "Tottenham", "Watford",
            "West Brom", "West Ham", "Wigan", "Wimbledon", "Wolves"]



def list_to_string_without_brackets(list1):
    return str(list1).replace('[','').replace(']','')



class type_of_statistics_head_to_head_exception(Exception):
    def __init__(self, type_of_statistics: str):
        self.type_of_statistics=type_of_statistics
        
@app.exception_handler(type_of_statistics_head_to_head_exception)
async def type_of_statistics_head_to_head_exception_handleR(
    request: Request, exc: type_of_statistics_head_to_head_exception):
    return JSONResponse(
        status_code=400,
        content={"message": "Please enter the type of statistics correctly. Available types of statistics: "  
                 + list_to_string_without_brackets(available_types_of_head_to_head_statistics) },
    )


class head_to_head_exception(Exception):
    def __init__(self, first_team: str, second_team= str):
        self.first_team = first_team
        self.second_team = second_team

@app.exception_handler(head_to_head_exception)
async def head_to_head_exception_handleR(request: Request, exc: head_to_head_exception):
    return JSONResponse(
        status_code=400,
        content={"message": "Please type the names of the teams correctly. The first letter of the team must be capitalized. Example: Arsenal- correct, arsenal- incorrect"},
    )



@app.get("/headtoheadstatistics/")
async def head_to_head_statistics(type_of_statistics: str, first_team: str, second_team: str):
    if type_of_statistics not in available_types_of_head_to_head_statistics:
        raise type_of_statistics_head_to_head_exception(type_of_statistics=type_of_statistics)
    else:
        if first_team not in all_teams:
            raise head_to_head_exception(first_team=first_team, second_team=second_team)
        if second_team not in all_teams:
            raise head_to_head_exception(first_team=first_team, second_team=second_team)    
        if first_team == second_team:
            raise head_to_head_exception(first_team=first_team, second_team=second_team)
        else:      
            df = hth.main_function_for_data_analysis(type_of_statistics, first_team, second_team)
            return df
    






# Football season statistics

available_types_of_football_season_statistics = ["all scores", "exact number of goals in the match", 
                                                 "goals over", "goals under", "home vs away full time result", 
                                                 "home vs away result first half and the match"]

all_seasons = ["2021/22", "2020/21", "2019/20", "2018/19", "2017/18", "2016/17", "2015/16", "2014/15", 
               "2013/14", "2012/13", "2011/12", "2010/11", "2009/10", "2008/09", "2007/08", "2006/07", 
               "2005/06", "2004/05", "2003/04", "2002/03", "2001/02", "2000/01", "1999/00", "1998/99", 
               "1997/98", "1996/97", "1995/96"]


class type_of_statistics_football_season_exception(Exception):
    def __init__(self, type_of_statistics: str):
        self.type_of_statistics=type_of_statistics
        
@app.exception_handler(type_of_statistics_football_season_exception)
async def type_of_statistics_football_season_exception_handleR(
    request: Request, exc: type_of_statistics_football_season_exception):
    return JSONResponse(
        status_code=400,
        content={"message": "Please enter the type of statistics correctly. Available types of statistics: "  
                 + list_to_string_without_brackets(available_types_of_football_season_statistics)},
    )


class football_season_exception(Exception):
    def __init__(self, season: str):
        self.season = season

@app.exception_handler(football_season_exception)
async def football_season_exception_handler(request: Request, exc: football_season_exception):
    return JSONResponse(
        status_code=400,
        content={"message": "Please type correctly the season. Choose one season from " + data.df["Season"].iloc[-0] +" to " + data.df["Season"].iloc[-1]},
    )


@app.get("/footballseasonstatistics/{type_of_statistics}/{season:path}" )
async def football_season_statistics(type_of_statistics:str, season: str):
    if type_of_statistics not in available_types_of_football_season_statistics:
        raise type_of_statistics_football_season_exception(type_of_statistics=type_of_statistics)
    if season not in all_seasons:
        raise football_season_exception(season=season)
    if season in all_seasons:
        df = sn.main_function_for_data_analysis(type_of_statistics, season)
        return df









# Team statistics

available_types_of_team_statistics = ["exact number of goals in the match", "result first half and the match",
                                      "goals over", "goals under", "home vs away full time result", 
                                      "full time result"]



class type_of_statistics_team_exception(Exception):
    def __init__(self, type_of_statistics: str):
        self.type_of_statistics = type_of_statistics
     
@app.exception_handler(type_of_statistics_team_exception)
async def type_of_statistics_team_exception_handleR(request: Request, exc: type_of_statistics_team_exception):
    return JSONResponse(
        status_code=400,
        content={"message": "Please enter the type of statistics correctly. Available types of statistics: "  
                 + list_to_string_without_brackets(available_types_of_team_statistics) },
    )


class team_exception(Exception):
    def __init__(self, team: str):
        self.team = team
     
@app.exception_handler(team_exception)
async def team_exception_handleR(request: Request, exc: team_exception):
    return JSONResponse(
        status_code=400,
        content={"message": "Please type the name of the team correctly."},
    )


@app.get("/teamstatistics/{type_of_statistics}/{team}")
async def team_statistics(type_of_statistics:str, team: str):
    if type_of_statistics not in available_types_of_team_statistics:
        raise type_of_statistics_team_exception(type_of_statistics = type_of_statistics)
    if team not in all_teams:
        raise team_exception(team=team)
    else:      
        df = tm.main_function_for_data_analysis(type_of_statistics, team)
        return df



