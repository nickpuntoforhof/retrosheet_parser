# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 12:46:49 2019

@author: woody
"""
# Import libraries
import os
import pandas as pd
os.chdir('C:/Users/woody/OneDrive/Documents/githubrepos/retrosheet_parser/code')
import get_player_positions_per_game as retro_parse

# Point to retrosheet files
os.chdir('C:/Users/woody/OneDrive/Documents/retrosheet/')

# Get list of files in subdirectory of all working directories
dirName = './'
listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk(dirName):
    loop_files = [os.path.join(dirpath, file).replace('\\','/') for file in filenames]
    listOfFiles.append(loop_files)
    
# This gives a list of lists, one for each directory.  Flatten
# the list
listOfFiles = [item for sublist in listOfFiles for item in sublist]

out = pd.DataFrame(columns=['retroID', 'playerName', 'teamID','gameDate',
                                'battingOrder','pos','dblhdr'])
    
first_year = 2008
last_year = 2019

for file in listOfFiles:
    if file[-4:] in [".EVA", ".EVN"]:
        year = int(file[-11:-7])
        if (year >= first_year) & (year <= last_year):
            print(file)
            
            loop_df = retro_parse.get_player_positions_per_game(file, 
                                                                verbose = False)
            out = pd.concat([out, loop_df])
            

os.chdir('C:/Users/woody/OneDrive/Documents/githubrepos/retrosheet_parser/data')
out.to_csv("player_positions_per_game_08_19.csv")

    