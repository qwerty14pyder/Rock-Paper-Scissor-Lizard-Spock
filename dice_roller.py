import random as r
import json
data = {}
with open('pastRolls.json', 'r') as f:
    data = json.load(fp=f)
def roll_dice(sides):
    roll = r.randint(1,sides)
    return roll
sides = int(input('How many sides are on your dice?(enter an interger > 1)\n>'))
roll = roll_dice(sides=sides)
print(f'That was roll {len(data)} and you rolled an {roll}')
data[len(data)] = roll
with open('pastRolls.json', 'w') as f:
    json.dump(data, fp=f, indent=4)