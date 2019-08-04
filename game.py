import random
import statistics

from utils import *

class POOL():
    def __init__(self):
        self.remaining_by_unit = {}
        self.remaining_by_cost = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0}

        for champion_id, d in CHAMPIONS.items():
            name = d["name"]
            cost = d["cost"]
            self.remaining_by_cost[cost] += POOL_TOTAL[cost]
            self.remaining_by_unit[name] = POOL_TOTAL[cost]

    def draw(self, cost):
        roll = random.randint(0, self.remaining_by_cost[cost] - 1)
        curr = 0

        # Iterate over champions
        for champion in CHAMPIONS_BY_TIER[cost]:
            curr += self.remaining_by_unit[champion]
            if roll < curr:
                return champion

    def pick(self, champion):
        name = champion["name"]
        cost = champion["cost"]

        if self.remaining_by_cost[cost] <= 0:
            raise Exception("No more units of this cost!")

        if self.remaining_by_unit[name] <= 0:
            raise Exception("No more units of this name!")

        self.remaining_by_cost[cost] -= 1
        self.remaining_by_unit[name] -= 1

    def put(self, champion):
        name = champion["name"]
        cost = champion["cost"]

        self.remaining_by_cost[cost] += 1
        self.remaining_by_unit[name] += 1


# How important are blockers?
# -- You have 50 gold and you are rolling for Ashe, how much do your chances
#    improve by holding on to all 3 cost units?
class GameState():
    def __init__(self, level, gold, board):
        self.level = level
        self.gold = gold
        self.pool = POOL()
        self.flop = []
        self.board = board

        self.roll_count = 0

    def get_flop(self):
        return self.flop

    def roll_cost(self):
        roll = random.randint(0, 999)
        curr = 0

        # Iterate over tiers of units
        for i in range(1, 6):
            curr += ROLL_CHANCE[self.level][i]
            if roll < curr: return i

        raise Exception("Should never reach here. Level: %d, roll: %d")

    def roll(self):
        if self.gold < 2:
            print("Not enough gold to roll")
            return None
        self.gold -= 2

        roll_cost = [self.roll_cost() for i in range(5)]
        roll_champions = [{"name" : self.pool.draw(cost), "cost" : cost} for cost in roll_cost]
        self.flop = roll_champions
        self.roll_count += 1

    def buy(self, champion):
        flop_names = [champ["name"] for champ in self.flop]
        if champion["name"] not in flop_names:
            raise Exception("Tried to buy champion not on the flop")

        if len(self.board) >= 10:
            raise Exception("Board limit exceeded, can't buy")

        # Update gold
        self.gold -= champion["cost"]

        # Update the flop
        for i in range(len(self.flop)):
            if self.flop[i]["name"] == champion["name"]:
                self.flop[i] = {'name' : "Taken", 'cost' : -1}
                break

        # Add it to the board
        self.board.append(champion)

        # Update the pool
        self.pool.pick(champion)

    def sell(self, champion):
        board_names = [champ["name"] for champ in self.board]
        if champion["name"] not in board_names:
            raise Exception("Tried to selff champion not on the board")

        # Update gold
        self.gold += champion["cost"]

        # Update the board
        self.board.remove(board_names.index(champion["name"]))

        # Update the pool
        self.pool.put(champion)

# This algorithm buys any lv3 unit until it finds an ashe
def bot1():
    gs = GameState(level=6, gold=100, board=[])
    found = 0

    while gs.gold >= 5 and not found:
        # roll,
        gs.roll()
        flop = gs.get_flop()
        for champ in flop:
            if champ["cost"] == 3 and len(gs.board) < 10:
                gs.buy(champ)

            if "Ashe" == champ["name"]:
                found = 1

    return gs.roll_count

# This algorithm rolls until it finds an ashe
def bot2():
    gs = GameState(level=6, gold=100, board=[])
    found = 0

    while gs.gold >= 5 and not found:
        gs.roll()
        for champ in gs.get_flop():
            if "Ashe" == champ["name"]:
                found = 1
                break

    return gs.roll_count

# You are lv 6 with 100 gold and trying to find a single Ashe
# What is the +EV in gold if you pick up every tier 3 unit along the way?
def experiment1():
    tot1 = []
    for i in range(100000):
        tot1.append(bot1())


    tot2 = []
    for i in range(100000):
        tot2.append(bot2())

    print("Avg rolls method1: ", sum(tot1)/100000)
    print("Avg rolls method2: ", sum(tot2)/100000)
    print("Stdev method1: ", statistics.stdev(tot1))
    print("Stdev method2: ", statistics.stdev(tot2))


# This algorithm buys any lv3 unit until it finds an ashe
def bot3():
    gs = GameState(level=7, gold=400, board=[])
    found = 0

    while gs.gold >= 5 and not found:
        gs.roll()
        for champ in gs.get_flop():
            if champ["cost"] == 4 and len(gs.board) < 10:
                gs.buy(champ)

            if "Cho'gath" == champ["name"]:
                found = 1

    return gs.roll_count

# This algorithm rolls until it finds an ashe
def bot4():
    gs = GameState(level=7, gold=400, board=[])
    found = 0

    while gs.gold >= 5 and not found:
        gs.roll()
        for champ in gs.get_flop():
            if "Cho'gath" == champ["name"]:
                found = 1
                break

    return gs.roll_count

# You are lv 7 with 400 gold and trying to find a single Cho
# What is the +EV in gold if you pick up every tier 4 unit along the way?
def experiment2():
    tot1 = []
    for i in range(100000):
        tot1.append(bot3())


    tot2 = []
    for i in range(100000):
        tot2.append(bot4())

    print("Avg rolls method1: ", sum(tot1)/100000)
    print("Avg rolls method2: ", sum(tot2)/100000)
    print("Stdev method1: ", statistics.stdev(tot1))
    print("Stdev method2: ", statistics.stdev(tot2))

# This algorithm buys any lv3 unit until it finds an ashe
def bot5():
    gs = GameState(level=8, gold=400, board=[])
    found = 0

    while gs.gold >= 5 and not found:
        gs.roll()
        for champ in gs.get_flop():
            if champ["cost"] == 5 and len(gs.board) < 10:
                gs.buy(champ)

            if "Kayle" == champ["name"]:
                found = 1

    return gs.roll_count

# This algorithm rolls until it finds an ashe
def bot6():
    gs = GameState(level=8, gold=400, board=[])
    found = 0

    while gs.gold >= 5 and not found:
        gs.roll()
        for champ in gs.get_flop():
            if "Kayle" == champ["name"]:
                found = 1
                break

    return gs.roll_count

# You are lv 7 with 400 gold and trying to find a single Cho
# What is the +EV in gold if you pick up every tier 4 unit along the way?
def experiment3():
    tot1 = []
    for i in range(100000):
        tot1.append(bot5())

    tot2 = []
    for i in range(100000):
        tot2.append(bot6())

    print("Avg rolls method1: ", sum(tot1)/100000)
    print("Avg rolls method2: ", sum(tot2)/100000)
    print("Stdev method1: ", statistics.stdev(tot1))
    print("Stdev method2: ", statistics.stdev(tot2))

experiment1()
experiment2()
experiment3()