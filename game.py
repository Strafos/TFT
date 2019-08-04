import random

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

    def buy(self, champion):
        flop_names = [champ["name"] for champ in flop]
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

        # Update the pool
        self.pool.pick(champion)

# You are lv 6 with 50 gold and trying to find a single Ashe
# What is the +EV in gold if you pick up every tier 3 unit along the way?
def experiment1():
    gs = GameState(level=6, gold=50, board=[])
    gs.roll()
    flop = gs.get_flop()
    print(flop)
    for champ in flop:
        if champ["cost"] == 3:
            gs.buy(champ)
            print(gs.get_flop())