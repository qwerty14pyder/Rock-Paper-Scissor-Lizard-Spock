import random
possible_choices = ["Rock", "Paper", "Scissor", "Lizard", "Spock"]
computer_choice = random.choice(possible_choices)
player_choice = input("player one input choice, no caps \n>")
if player_choice == "rock" and computer_choice == "Scissor" or "Lizard":
    print("You win!")
elif player_choice == "paper" and computer_choice == "Rock" or "Spock":
    print("You Win!")
