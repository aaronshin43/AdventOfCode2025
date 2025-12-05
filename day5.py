# https://adventofcode.com/2025/day/5
'''
3-5
10-14
16-20
12-18

1
5
8
11
17
32
'''
freshIDs = []
ingredientIDs = []

while True:
    freshID = input()
    if not freshID:
        break
    freshIDs.append(freshID)

while True:
    ingredientID = input()
    if not ingredientID:
        break
    ingredientIDs.append(ingredientID)

#print(freshIDs)
#print(ingredientIDs)

for i in range(len(freshIDs)):
    temp = freshIDs[i].split('-')
    freshIDs[i] = [int(temp[0]), int(temp[1])]

#print(freshIDs)

# Part 1
# count = 0
# for i in ingredientIDs:
#     for j in freshIDs:
#         if int(i) >= j[0] and int(i) <= j[1]:
#             #print(i)
#             count += 1
#             break
# print(count)

# Part2 (Doesn't work)
# uniqueFreshIDs = {}
# for i in range(len(freshIDs)):
#     for j in range(freshIDs[i][0], freshIDs[i][1]+1):
#         if uniqueFreshIDs.get(j, 0) == 0:
#             uniqueFreshIDs[j] = 1

# print(len(uniqueFreshIDs.keys()))

# Real Part 2
cleanRange = []
count = 0
for i in range(len(freshIDs)):
    cleanLower = freshIDs[i][0]
    cleanUpper = freshIDs[i][1]
    for j in range(len(cleanRange)):
        lowerRange = cleanLower >= cleanRange[j][0] and cleanLower <= cleanRange[j][1]
        upperRange = cleanUpper >= cleanRange[j][0] and cleanUpper <= cleanRange[j][1]
        coverRange = cleanLower < cleanRange[j][0] and cleanUpper > cleanRange[j][1]
        if coverRange:
            cleanRange[j] = [0, -1]
        elif lowerRange and upperRange:
            break
        elif lowerRange:
            cleanLower = cleanRange[j][1]+1
        elif upperRange:
            cleanUpper = cleanRange[j][0]-1
    else:
        if cleanLower <= cleanUpper:
            cleanRange.append([cleanLower, cleanUpper])
    #print(cleanRange)
for i in cleanRange:
    count += i[1]-i[0]+1
print(count)
'''

50-70
44-58
55-57
43-59
44-62
1-100


'''