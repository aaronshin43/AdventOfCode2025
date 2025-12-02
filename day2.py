# https://adventofcode.com/2025/day/2
ID = input().split(",")
#print(ID)
result = 0
while ID:
    currentRange = ID.pop()
    firstID = int(currentRange[:currentRange.index('-')])
    #print(firstID)
    lastID = int(currentRange[currentRange.index('-')+1:])
    #print(lastID)
    for i in range(firstID, lastID+1):
        #print(i)
        currentID = str(i)
        if len(currentID) % 2 != 0:
            continue

        if currentID[0] == '0':
            result += i
            continue
        
        firstHalf = currentID[:len(currentID)//2]
        #print(firstHalf)
        secondHalf = currentID[len(currentID)//2:]
        #print(secondHalf)
        if firstHalf == secondHalf:
            #print(f"INVALID ID: {currentID}")
            result += i

print(result)