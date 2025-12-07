# https://adventofcode.com/2025/day/7

'''
.......S.......
............... 
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^.... 
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
'''

tachyonManifold: list[list[str]] = []
while True:
    tachyon = list(input())
    if not tachyon:
        break
    tachyonManifold.append(tachyon)

# for i in tachyonManifold:
#     print(i)

startPos = tachyonManifold[0].index('S')
tachyonManifold[1][startPos] = '|'

# Part 1
# count = 0
# for i in range(1, len(tachyonManifold)-1):
#     for j in range(len(tachyonManifold[i])):
#         if tachyonManifold[i][j] == "|":
#             if tachyonManifold[i+1][j] == "^":
#                 count += 1
#                 tachyonManifold[i+1][j-1] = "|"
#                 tachyonManifold[i+1][j+1] = "|"
#             elif tachyonManifold[i+1][j] == ".":
#                 tachyonManifold[i+1][j] = "|"
# for i in tachyonManifold:
#     print(i)
# print(count)

# Part 2 DFS (Too slow)
# count = 0
# path = [(1, startPos)]
# while path:
#     currX, currY = path.pop()
#     #print(currX, currY)
#     if currX == len(tachyonManifold)-1:
#         count += 1
#         continue

#     if tachyonManifold[currX+1][currY] == "^":
#         path.append((currX+1, currY+1))
#         path.append((currX+1, currY-1))
#     elif tachyonManifold[currX+1][currY] == ".":
#         path.append((currX+1, currY))
#     #print(path)
# print(count)

from collections import deque
from functools import cache

@cache
def score(x, y):
    if x == len(tachyonManifold)-1:
        return 1
    if tachyonManifold[x+1][y] == "^":
        return score(x+1, y-1) + score(x+1, y+1)
    else:
        return score(x+1, y)

# No need to find each path
# queue = deque([(1, startPos)])
# VISITED = set()
# while queue:
#     currX, currY = queue.popleft()
#     if (currX, currY) in VISITED:
#         continue
#     #print(currX, currY)
#     VISITED.add((currX, currY))
#     if currX == len(tachyonManifold)-1:
#         continue
#     if tachyonManifold[currX+1][currY] == "^":
#         queue.append((currX+1, currY+1))
#         queue.append((currX+1, currY-1))
#     elif tachyonManifold[currX+1][currY] == ".":
#         queue.append((currX+1, currY))
# print(queue)
print(score(1, startPos))
