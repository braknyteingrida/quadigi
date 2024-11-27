from pprint import pprint as pprint
import random

dim = 10
grid = []
for _ in range(dim):
    line = []
    for _ in range(dim):
        state = random.choice([0, 1])
        line.append(state)
    grid.append(line)
    
    
pprint(grid)

# for arr in grid:
#     index1=grid.index(arr)
#     #print(index1)
#     for idx, elem in enumerate(arr):
#         #print(elem, "indeksas", idx)
#         index2 = idx
#         if elem == 1:
#             print(index2, index1)
            
#             print(grid[index1][index2])
#     break
    
# def neighbor_count(ind1:int, ind2:int) -> int: 
#     if ind1 == 0 or (dim-1) & ind2 == 0 or(dim-1):
#         return 2
#     elif ind1 == 0 or (dim-1) & ind2 > 0 & ind2<(dim-1):
#         return 3
    
# nice = neighbor_count(9,4)
# print(nice)

for dy in [-1, 0, 1]:
    for dx in [-1, 0, 1]:
        if dx == 0 and dx == 0:
            continue
        x = x+ dx
        y = y +dx