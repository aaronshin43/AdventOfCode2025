start = 50
count = 0

N = 10
rotations = [input() for _ in range(N)]

rotations = rotations[::-1]
#print(rotations)

while rotations:
    rotation = rotations.pop()
    direction = rotation[0]
    number = int(rotation[1:])
    #print(direction, number)

    if direction == "L":
        continue

    if direction == "R":
        continue