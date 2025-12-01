position = 50
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

    for _ in range(number):
        if direction == "L":
            position = (position - 1) % 100

        if direction == "R":
            position = (position + 1) % 100
        
        if position == 0:
            count += 1

    #print(f"rotation: {rotation} / position: {position} / count: {count}")
    
print(count)