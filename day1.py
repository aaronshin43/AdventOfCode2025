start = 50
count = 0

rotations = []
while True:
    temp = input()

    if not temp:
        break
    rotations.append(temp)

rotations = rotations[::-1]
#print(rotations)

while rotations:
    rotation = rotations.pop()
    direction = rotation[0]
    number = int(rotation[1:])
    #print(direction, number)

    if direction == "L":
        number *= -1

    start = (start + number) % 100
    #print(start)
    if start == 0:
        count += 1

print(count)