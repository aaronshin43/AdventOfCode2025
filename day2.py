# https://adventofcode.com/2025/day/2
import math

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
        # if len(currentID) % 2 != 0:
        #     continue
        
        if currentID[0] == '0':
            print(f"INVALID ID: {currentID}")
            result += i
            continue
        
        # firstHalf = currentID[:len(currentID)//2]
        # #print(firstHalf)
        # secondHalf = currentID[len(currentID)//2:]
        # #print(secondHalf)
        # if firstHalf == secondHalf:
        #     #print(f"INVALID ID: {currentID}")
        #     result += i
        
        divisors = [j for j in range(1, len(currentID) + 1) if len(currentID) % j == 0]
        #print(divisors)
        divisors.pop()
        while divisors:
            currentDivisor = divisors.pop()
            recursiveTerm = currentID[:currentDivisor]
            #print(recursiveTerm)
            Invalid = True
            for j in range(len(currentID)):
                if recursiveTerm[j%len(recursiveTerm)] != currentID[j]:
                    Invalid = False
            if Invalid:
                #print(f"INVALID ID: {currentID}")
                result += i
                divisors = []
        #print("=======================================")


print(result)

#11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124