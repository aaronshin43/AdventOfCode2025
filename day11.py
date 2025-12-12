# https://adventofcode.com/2025/day/11
'''
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
'''

graph = {}
while True:
    line = input()
    if not line:
        break
    parts = line.split(': ')
    device = parts[0]
    outputs = parts[1].split()
    graph[device] = outputs

# print(graph)

# Part 1 DFS
def count_paths(current, target, graph):
    # print(current)
    if current == target:
        return 1
    
    total = 0
    for next_device in graph[current]:
        # print(next_device)
        total += count_paths(next_device, target, graph)
    return total

result = count_paths('you', 'out', graph)
print(result)
