#imports that are needed for this to work
import random as r

#generats a random number
def random_num():
    return r.randint(0,4)

#defines all the options
options = ['rock', 'paper', 'scissors', 'lizard', 'spock']


ai_choice = options[random_num()]



player_choice = int(input('What do you want to choose? (use the number presented with your choice\n1 rock\n2 paper\n3 scissors\n4 lizard\n5 spock\n>'))
player_choice -= 1
player_choice = options[player_choice]



if player_choice == 'rock' and ai_choice ==  'lizard' or ai_choice == 'scissors':
    print(f"Congradulations {player_choice} beats {ai_choice} you win !")
elif player_choice == 'paper' and ai_choice == 'rock' or ai_choice == 'spock':
    print(f"Congradulations {player_choice} beats {ai_choice} you win !")
elif player_choice == 'scissors' and ai_choice == 'paper' or ai_choice == 'lizard':
    print(f"Congradulations {player_choice} beats {ai_choice} you win !")
elif player_choice == 'lizard' and ai_choice == 'paper' or ai_choice == 'spock':
    print(f"Congradulations {player_choice} beats {ai_choice} you win !")
elif player_choice == 'spock' and ai_choice == 'rock' or ai_choice == 'scissors':
    print(f"Congradulations {player_choice} beats {ai_choice} you win !")
else:
    print(f'Sorry {ai_choice} beats {player_choice} you lose :(')