# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 11:00:44 2019

This script defines a function that takes a
retrosheet file and outputs each players position(s)
for each game in the file

@author: Noah Stafford
"""
# Libraries

import pandas as pd

# Creating an empty Dataframe with column names only

def get_player_positions_per_game(file, verbose=False):
    
    # Create empty dataframe to append to
    out = pd.DataFrame(columns=['retroID', 'playerName', 'teamID','gameDate',
                                'battingOrder','pos','dblhdr'])
    
    with open(file) as fp:
       line = fp.readline()
       cnt = 1
       while line:
           line_vector = line.strip().split(",")
           record_type = line_vector[0]
           second_entry = line_vector[1]
           
           if record_type == 'id':
               game_id = line_vector[1]
               #home_team = game_id[0:3]
               year = game_id[3:7]
               month = game_id[7:9]
               day = game_id[9:11]
               dblhdr = game_id[11:12]
               gameDate = year + "-" + month + "-" + day
               cnt += 1
               if verbose: print(game_id, gameDate, dblhdr)
             
           # get home and away teamIDs
           if (record_type == "info") & (second_entry == "hometeam"):
              home_team = line_vector[2]
          
           if (record_type == "info") & (second_entry == "visteam"):
              away_team = line_vector[2]
           
           # All records with info about lineup change will start with
           # 'start' or 'sub'
           if record_type in ['start','sub']:
               retroID = line_vector[1]
               playerName = line_vector[2]
               home_bool = line_vector[3]
               battingOrder = line_vector[4]
               pos = line_vector[5]
               
               teamID = home_team if home_bool == 0 else away_team
               
               out_row = pd.DataFrame({"retroID": [retroID], 
                         "playerName": [playerName],
                         "teamID": [teamID],
                         "gameDate": [gameDate],
                         "battingOrder": [battingOrder],
                         "pos": [pos],
                         "dblhdr": [dblhdr]})
               if verbose: print(out_row)
               
               out = pd.concat([out, out_row]) # concatenate output and new row
               
           
           line = fp.readline()
           #cnt += 1
           
    print(cnt, " Games Parsed")
    return out