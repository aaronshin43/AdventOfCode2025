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

count = 0
for i in range(1, len(tachyonManifold)-1):
    for j in range(len(tachyonManifold[i])):
        if tachyonManifold[i][j] == "|":
            if tachyonManifold[i+1][j] == "^":
                count += 1
                tachyonManifold[i+1][j-1] = "|"
                tachyonManifold[i+1][j+1] = "|"
            elif tachyonManifold[i+1][j] == ".":
                tachyonManifold[i+1][j] = "|"
for i in tachyonManifold:
    print(i)
print(count)
