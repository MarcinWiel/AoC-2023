import pandas as pd
import re

input_file = open("day2-23-input.txt", "r")
games = input_file.read()

# only 12 red cubes, 13 green cubes, and 14 blue cubes

games_list = list(games.split("\n"))
for i in range (0, len(games_list)):
    games_list[i] = games_list[i].replace(' red', '-12')
    games_list[i] = games_list[i].replace(' green', '-13')
    games_list[i] = games_list[i].replace(' blue', '-14')

for i in range(0,9):
    games_list[i] = games_list[i][8:]
for i in range(9,99):
    games_list[i] = games_list[i][9:]
for i in range(99,100):
    games_list[i] = games_list[i][10:]
for i in range (0, len(games_list)):
    games_list[i] = re.split('; |, ', games_list[i])

for i in range(0, len(games_list)):
    for k in range(0, len(games_list[i])):
        games_list[i][k] = eval(games_list[i][k])

df = pd.DataFrame(games_list)

#df.insert(0, 'id', range(1, 101))
df = df.fillna(0).astype(int)

### ZROBIĆ WARTOŚCI DODATNIE DLA RZĘDÓW
matches = df[(df <= 0).all(axis=1)]

matches_index = list(matches.index.values)

for i in range(0, len(matches_index)):
    matches_index[i] = matches_index[i]+1

result = sum(matches_index)

print(result)


#########




# poprzednie próby

# id_to_remove = []

# ###
# df_red = df
# df_red = df_red.replace(regex={r'blue$': None, 'green$': None})

# for i in range(0,18):
#     df_red[i] = df_red[i].str[:-4]

# df_red = df_red.fillna(0).astype(int)
# df_red['total']= df_red.iloc[:, -18:-1].sum(axis=1)

# df_red_remove = df_red.loc[df_red['total'] > 12]

# red_ids_remove = df_red_remove['id'].values.tolist()
# for i in red_ids_remove:
#     id_to_remove.append(i)
# ###

# ###
# df_green = df
# df_green = df_green.replace(regex={r'blue$': None, 'red$': None})

# for i in range(0,18):
#     df_green[i] = df_green[i].str[:-6]

# df_green = df_green.fillna(0).astype(int)
# df_green['total']= df_green.iloc[:, -18:-1].sum(axis=1)

# df_green_remove = df_green.loc[df_green['total'] > 13]

# green_ids_remove = df_green_remove['id'].values.tolist()
# for i in green_ids_remove:
#     id_to_remove.append(i)
# ###

# ###
# df_blue = df
# df_blue = df_blue.replace(regex={r'green$': None, 'red$': None})

# for i in range(0,18):
#     df_blue[i] = df_blue[i].str[:-5]

# df_blue = df_blue.fillna(0).astype(int)
# df_blue['total']= df_blue.iloc[:, -18:-1].sum(axis=1)

# df_blue_remove = df_blue.loc[df_blue['total'] > 14]

# blue_ids_remove = df_blue_remove['id'].values.tolist()
# for i in blue_ids_remove:
#     id_to_remove.append(i)
# ###

# df_good = df.loc[~df['id'].isin(id_to_remove)]

# print(df_good)