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

count = 0
for i in ingredientIDs:
    for j in freshIDs:
        if int(i) >= j[0] and int(i) <= j[1]:
            #print(i)
            count += 1
            break
print(count)