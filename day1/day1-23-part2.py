from re import *

# d = {'zero' : '0', 'one' : '1'}
# s = ['keightwo25hmqthbeight']
# l = ['zero', 'one']

# sol = []

# for line in range (0, len(s)):
#     for letter in range(len(s[line])):
#         try:    
#             if s[line][letter] == 'e':
#                 if s[line][letter+1] == 'i':
#                     if s[line][letter+2] == 'g':
#                         if s[line][letter+3] == 'h':
#                             if s[line][letter+4] == 't':
#                                 sol.append('8')
#                                 break
#             if s[line][letter] == 't':
#                 if s[line][letter+1] == 'w':
#                     if s[line][letter+2] == 'o':
#                             sol.append('2')
#                             break
#         except IndexError:
#             continue

# print(sol)
# finder = ''
# for line in range (len(s)):
#     for i in range (0, len(l)):    
#         s[line] = map(lambda x: sub(l[i], '0', x), s)

# print(list(s))

input_file = open("day1-23-input.txt", "r")
calibration = input_file.read()

s = list(calibration.split("\n"))

coord_list = []

for line in range (0, len(s)):
    for letter in range(len(s[line])):
        try:    
            if s[line][letter] == 'z':
                if s[line][letter+1] == 'e':
                    if s[line][letter+2] == 'r':
                        if s[line][letter+3] == 'o':
                            coord_list.append('0')
                            break
            if s[line][letter] == 'o':
                if s[line][letter+1] == 'n':
                    if s[line][letter+2] == 'e':
                            coord_list.append('1')
                            break
            if s[line][letter] == 't':
                if s[line][letter+1] == 'w':
                    if s[line][letter+2] == 'o':
                        coord_list.append('2')
                        break
            if s[line][letter] == 't':
                if s[line][letter+1] == 'h':
                    if s[line][letter+2] == 'r':
                        if s[line][letter+3] == 'e':
                            if s[line][letter+4] == 'e':
                                coord_list.append('3')
                                break
            if s[line][letter] == 'f':
                if s[line][letter+1] == 'o':
                    if s[line][letter+2] == 'u':
                        if s[line][letter+3] == 'r':
                            coord_list.append('4')
                            break
            if s[line][letter] == 'f':
                if s[line][letter+1] == 'i':
                    if s[line][letter+2] == 'v':
                        if s[line][letter+3] == 'e':
                            coord_list.append('5')
                            break
            if s[line][letter] == 's':
                if s[line][letter+1] == 'i':
                    if s[line][letter+2] == 'x':
                        coord_list.append('6')
                        break
            if s[line][letter] == 's':
                if s[line][letter+1] == 'e':
                    if s[line][letter+2] == 'v':
                        if s[line][letter+3] == 'e':
                            if s[line][letter+4] == 'n':
                                coord_list.append('7')
                                break
            if s[line][letter] == 'e':
                if s[line][letter+1] == 'i':
                    if s[line][letter+2] == 'g':
                        if s[line][letter+3] == 'h':
                            if s[line][letter+4] == 't':
                                coord_list.append('8')
                                break
            if s[line][letter] == 'n':
                if s[line][letter+1] == 'i':
                    if s[line][letter+2] == 'n':
                        if s[line][letter+3] == 'e':
                            coord_list.append('9')
                            break
            if s[line][letter] == '0':
                coord_list.append('0')
                break
            if s[line][letter] == '1':
                coord_list.append('1')
                break
            if s[line][letter] == '2':
                coord_list.append('2')
                break  
            if s[line][letter] == '3':
                coord_list.append('3')
                break  
            if s[line][letter] == '4':
                coord_list.append('4')
                break  
            if s[line][letter] == '5':
                coord_list.append('5')
                break  
            if s[line][letter] == '6':
                coord_list.append('6')
                break  
            if s[line][letter] == '7':
                coord_list.append('7')
                break  
            if s[line][letter] == '8':
                coord_list.append('8')
                break  
            if s[line][letter] == '9':
                coord_list.append('9')
                break                                                               
        except IndexError:
            continue

rev_coord_list = []

r = list(s[i][::-1] for i in range (0, len(s)))

for line in range (0, len(r)):
    for letter in range(len(r[line])):
        try:    
            if r[line][letter] == 'o':
                if r[line][letter+1] == 'r':
                    if r[line][letter+2] == 'e':
                        if r[line][letter+3] == 'z':
                            rev_coord_list.append('0')
                            break
            if r[line][letter] == 'e':
                if r[line][letter+1] == 'n':
                    if r[line][letter+2] == 'o':
                            rev_coord_list.append('1')
                            break
            if r[line][letter] == 'o':
                if r[line][letter+1] == 'w':
                    if r[line][letter+2] == 't':
                        rev_coord_list.append('2')
                        break
            if r[line][letter] == 'e':
                if r[line][letter+1] == 'e':
                    if r[line][letter+2] == 'r':
                        if r[line][letter+3] == 'h':
                            if r[line][letter+4] == 't':
                                rev_coord_list.append('3')
                                break
            if r[line][letter] == 'r':
                if r[line][letter+1] == 'u':
                    if r[line][letter+2] == 'o':
                        if r[line][letter+3] == 'f':
                            rev_coord_list.append('4')
                            break
            if r[line][letter] == 'e':
                if r[line][letter+1] == 'v':
                    if r[line][letter+2] == 'i':
                        if r[line][letter+3] == 'f':
                            rev_coord_list.append('5')
                            break
            if r[line][letter] == 'x':
                if r[line][letter+1] == 'i':
                    if r[line][letter+2] == 's':
                        rev_coord_list.append('6')
                        break
            if r[line][letter] == 'n':
                if r[line][letter+1] == 'e':
                    if r[line][letter+2] == 'v':
                        if r[line][letter+3] == 'e':
                            if r[line][letter+4] == 's':
                                rev_coord_list.append('7')
                                break
            if r[line][letter] == 't':
                if r[line][letter+1] == 'h':
                    if r[line][letter+2] == 'g':
                        if r[line][letter+3] == 'i':
                            if r[line][letter+4] == 'e':
                                rev_coord_list.append('8')
                                break
            if r[line][letter] == 'e':
                if r[line][letter+1] == 'n':
                    if r[line][letter+2] == 'i':
                        if r[line][letter+3] == 'n':
                            rev_coord_list.append('9')
                            break
            if r[line][letter] == '0':
                rev_coord_list.append('0')
                break
            if r[line][letter] == '1':
                rev_coord_list.append('1')
                break
            if r[line][letter] == '2':
                rev_coord_list.append('2')
                break  
            if r[line][letter] == '3':
                rev_coord_list.append('3')
                break  
            if r[line][letter] == '4':
                rev_coord_list.append('4')
                break  
            if r[line][letter] == '5':
                rev_coord_list.append('5')
                break  
            if r[line][letter] == '6':
                rev_coord_list.append('6')
                break  
            if r[line][letter] == '7':
                rev_coord_list.append('7')
                break  
            if r[line][letter] == '8':
                rev_coord_list.append('8')
                break  
            if r[line][letter] == '9':
                rev_coord_list.append('9')
                break                                                               
        except IndexError:
            continue


true_coords = [coord_list[i] + rev_coord_list[i] for i in range(0, 1000)]
#print(true_coords)

int_coords = [int(true_coords[i]) for i in range(0, 1000)]
print(int_coords)

result = 0

for i in range (0, 1000):
    result += int_coords[i]

print(result)