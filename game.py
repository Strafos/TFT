import random

# For a given level, what are the chances of rolling a 1-5 tier unit
ROLL_CHANCE = {
    2 : [100, 0, 0, 0, 0],
    3 : [65, 30, 5],
    4 : [50, 35, 15],
    5 : [37, 35, 25, 3],
    6 : [24.5, 35, 30, 10, 0.5],
    7 : [20, 30, 33, 15, 2],
    8 : [15, 25, 35, 20, 5],
    9 : [10, 15, 35, 30, 10],
}

POOL_TOTAL = {
    1 : 39,
    2 : 26,
    3 : 21,
    4 : 13,
    5 : 10,
}

print(POOL_TOTAL[3])