# https://adventofcode.com/2025/day/2
ID = input().split(",")
#print(ID)
while ID:
    current = ID.pop()
    firstID = int(current[:current.index('-')])
    #print(firstID)
    lastID = int(current[current.index('-')+1:])
    #print(lastID)
    for i in range(firstID, lastID+1):
        #print(i)
        continue