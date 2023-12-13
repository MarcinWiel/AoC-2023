from re import *

input_file = open("day1-23-input.txt", "r")
calibration = input_file.read()

calib_list = list(calibration.split("\n"))

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
digit_dict = {
    "zero": '0',
    "two": '2',
    "three": '3',
    "nine": '9',
    "five": '5',
    "one": '1',
    "eight": '8',  
    "four": '4',
    "six": '6',
    "seven": '7'
}

for line in range (0, len(calib_list)):
    for key in digit_dict:
        calib_list[line] = sub(key, digit_dict[key], calib_list[line])

#print(calib_list)

coord_str = ''

for line in calib_list:
    for symbol in line:
        if symbol not in digits:
            continue
        if symbol in digits:
            coord_str += symbol
    coord_str += '\n'

#print(coord_str)

coord_list = list(coord_str.split("\n"))

for i in range (0, len(coord_list)):
    if len(coord_list[i]) in (0, 2):
        continue
    else:
        coord_list[i] = coord_list[i][0] + coord_list[i][-1]

coord_list.remove('')

print(coord_list[213])

coord_sum = 0

for i in range (0, len(coord_list)):
    coord_list[i] = int(coord_list[i])
    coord_sum += coord_list[i]

print(coord_sum)