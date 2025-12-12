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
# def count_paths(current, target, graph):
#     # print(current)
#     if current == target:
#         return 1
    
#     total = 0
#     for next_device in graph[current]:
#         # print(next_device)
#         total += count_paths(next_device, target, graph)
#     return total

# result = count_paths('you', 'out', graph)
# print(result)


'''
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
'''
# Part 2
from functools import cache

@cache
def count_paths2(current, visited_dac, visited_fft):
    # print(f"current: {current}")
    if current == 'dac':
        visited_dac = True
    if current == 'fft':
        visited_fft = True
    
    if current == 'out':
        # print(f"dac: {visited_dac}, fft: {visited_fft}")
        if visited_dac and visited_fft:
            return 1
        return 0
    
    total = 0
    for next_device in graph[current]:
        total += count_paths2(next_device, visited_dac, visited_fft)
    return total

result2 = count_paths2('svr', False, False)
print(result2)
