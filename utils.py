import random

# For a given level, what are the chances of rolling a 1-5 tier unit
# Each number is chance out of 1000
ROLL_CHANCE = {
    2 : {1 : 1000, 2 : 0, 3 : 0, 4 : 0, 5 : 0},
    3 : {1 : 650, 2 : 300, 3 : 50, 4 : 0, 5 : 0},
    4 : {1 : 500, 2 : 350, 3 : 150, 4 : 0, 5 : 0},
    5 : {1 : 370, 2 : 350, 3 : 250, 4 : 30, 5 : 0},
    6 : {1 : 245, 2 : 350, 3 : 300, 4 : 100, 5 : 5},
    7 : {1 : 200, 2 : 300, 3 : 330, 4 : 150, 5 : 20},
    8 : {1 : 150, 2 : 250, 3 : 350, 4 : 200, 5 : 50},
    9 : {1 : 100, 2 : 150, 3 : 350, 4 : 300, 5 : 100},
}

for k, v in ROLL_CHANCE.items():
    count = 0
    for k2, v2 in v.items():
        count += v2
    if count != 1000:
        raise Exception("Roll chance for tier %d does not add up to 1000", k)

POOL_TOTAL = {
    1 : 39,
    2 : 26,
    3 : 21,
    4 : 13,
    5 : 10,
}

CHAMPIONS = {
    1  : {"name" : "Aurelion Sol", "cost" : 4},
    2  : {"name" : "Brand", "cost" : 4},
    3  : {"name" : "Cho'gath", "cost" : 4},
    4  : {"name" : "Draven", "cost" : 4},
    5  : {"name" : "Gnar", "cost" : 4},
    6  : {"name" : "Kayle", "cost" : 5},
    7  : {"name" : "Pyke", "cost" : 2},
    8  : {"name" : "Sejuani", "cost" : 4},
    9  : {"name" : "Swain", "cost" : 5},
    10 : {"name" :  "Ahri", "cost" : 2},
    11 : {"name" :  "Darius", "cost" : 1},
    12 : {"name" :  "Garen", "cost" : 1},
    13 : {"name" :  "Kassadin", "cost" : 1},
    14 : {"name" :  "Kindred", "cost" : 4},
    15 : {"name" :  "Lissandra", "cost" : 2},
    16 : {"name" :  "Lucian", "cost" : 2},
    17 : {"name" :  "Lulu", "cost" : 2},
    18 : {"name" :  "Nidalee", "cost" : 1},
    19 : {"name" :  "Shen", "cost" : 2},
    20 : {"name" :  "Shyvana", "cost" : 3},
    21 : {"name" :  "Vayne", "cost" : 1},
    22 : {"name" :  "Varus", "cost" : 2},
    23 : {"name" :  "Yasuo", "cost" : 5},
    24 : {"name" :  "Aatrox", "cost" : 3},
    25 : {"name" :  "Akali", "cost" : 4},
    26 : {"name" :  "Ashe", "cost" : 3},
    27 : {"name" :  "Anivia", "cost" : 5},
    28 : {"name" :  "Blitzcrank", "cost" : 2},
    29 : {"name" :  "Braum", "cost" : 2},
    30 : {"name" :  "Graves", "cost" : 1},
    31 : {"name" :  "Kha'Zix", "cost" : 1},
    32 : {"name" :  "Kennen", "cost" : 3},
    33 : {"name" :  "Leona", "cost" : 4},
    34 : {"name" :  "Miss Fortune", "cost" : 5},
    35 : {"name" :  "Morgana", "cost" : 3},
    36 : {"name" :  "Warwick", "cost" : 1},
    37 : {"name" :  "Zed", "cost" : 2},
    38 : {"name" :  "Volibear", "cost" : 2},
    39 : {"name" :  "Elise", "cost" : 1},
    40 : {"name" :  "Evelynn", "cost" : 3},
    41 : {"name" :  "Fiora", "cost" : 1},
    42 : {"name" :  "Gangplank", "cost" : 3},
    43 : {"name" :  "Karthus", "cost" : 5},
    44 : {"name" :  "Katarina", "cost" : 3},
    45 : {"name" :  "Mordekaiser", "cost" : 1},
    46 : {"name" :  "Poppy", "cost" : 3},
    47 : {"name" :  "Rek'Sai", "cost" : 2},
    48 : {"name" :  "Rengar", "cost" : 3},
    49 : {"name" :  "Tristana", "cost" : 1},
    50 : {"name" :  "Veigar", "cost" : 3},
    50 : {"name" :  "Twisted Fate", "cost" : 2,}
}

TIER1_CHAMPIONS = [v["name"] for k, v in CHAMPIONS.items() if v["cost"] == 1]
TIER2_CHAMPIONS = [v["name"] for k, v in CHAMPIONS.items() if v["cost"] == 2]
TIER3_CHAMPIONS = [v["name"] for k, v in CHAMPIONS.items() if v["cost"] == 3]
TIER4_CHAMPIONS = [v["name"] for k, v in CHAMPIONS.items() if v["cost"] == 4]
TIER5_CHAMPIONS = [v["name"] for k, v in CHAMPIONS.items() if v["cost"] == 5]

CHAMPIONS_BY_TIER = {
    1 : TIER1_CHAMPIONS,
    2 : TIER2_CHAMPIONS,
    3 : TIER3_CHAMPIONS,
    4 : TIER4_CHAMPIONS,
    5 : TIER5_CHAMPIONS,
}