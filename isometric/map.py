import random

x = 14
y = 14

map_tileset = [[0 for i in range(y)] for i in range(x)]

for row_index in range(x):
    for column_index in range(y):
        map_tileset[row_index][column_index] = random.randint(0, 20)