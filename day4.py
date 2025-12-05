rolls = []
while True:
    roll = list(input())
    if not roll:
        break
    rolls.append(roll)

#print(rolls)
moveX = [-1, 0, 1, -1, 1, -1, 0, 1]
moveY = [-1, -1, -1, 0, 0, 1, 1, 1]
'''
1 2 3
4   5
6 7 8
'''

count = 0
for i in range(len(rolls)):
    for j in range(len(rolls[i])):
        # print(i, j)
        neighbors = 8
        for k in range(8):
            if rolls[i][j] == "@":
                neighborX, neighborY = j+moveX[k], i+moveY[k]
                # print(neighborX, neighborY)
                if neighborX < 0 or neighborX >= len(rolls[i]) or neighborY < 0 or neighborY >= len(rolls):
                    neighbors -= 1
                    # print("neighbor-1")
                elif rolls[neighborY][neighborX] == ".":
                    neighbors -= 1
                    # print("neighbor-1")
            else:
                # print("Not @")
                break
        # print(f"neighbors: {neighbors}")
        if neighbors < 4:
            count += 1
    #     print(f"Current: {count}")
    #     print("---------------")
    # print("====================")

print(count)