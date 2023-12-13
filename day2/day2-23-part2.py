import pandas as pd
import re
import numpy as np


input_file = open("day2-23-input.txt", "r")
games = input_file.read()

games_list = list(games.split("\n"))

for i in range(0,9):
    games_list[i] = games_list[i][8:]
for i in range(9,99):
    games_list[i] = games_list[i][9:]
for i in range(99,100):
    games_list[i] = games_list[i][10:]
for i in range (0, len(games_list)):
    games_list[i] = re.split('; |, ', games_list[i])

df = pd.DataFrame(games_list)


###
df_red = df
df_red = df_red.replace(regex={r'blue$': None, 'green$': None})

for i in range(0,18):
    df_red[i] = df_red[i].str[:-4]

df_red = df_red.fillna(0).astype(int) 
df_red['max_red']= df_red.max(axis=1)
###

###
df_green = df
df_green = df_green.replace(regex={r'blue$': None, 'red$': None})

for i in range(0,18):
    df_green[i] = df_green[i].str[:-6]

df_green = df_green.fillna(0).astype(int) 
df_green['max_green']= df_green.max(axis=1)
###

###
df_blue = df
df_blue = df_blue.replace(regex={r'green$': None, 'red$': None})

for i in range(0,18):
    df_blue[i] = df_blue[i].str[:-5]

df_blue = df_blue.fillna(0).astype(int) 
df_blue['max_blue']= df_blue.max(axis=1)
###

df['max_red'] = df_red['max_red']
df['max_green'] = df_green['max_green']
df['max_blue'] = df_blue['max_blue']

df_max = df[['max_red', 'max_green', 'max_blue']]
df_max['power'] = df_max['max_red']*df_max['max_green']*df_max['max_blue']
print(sum(df_max['power']))