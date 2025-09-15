import random as r
def roll_dice(sides):
    roll = r.randint(1,sides)
    return roll
sides = int(input('How many sides are on your dice?(enter an interger > 1)\n>'))
roll = roll_dice(sides=sides)
print(roll)