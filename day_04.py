import random
from random import randint

# import random
# import my_module
#
# random_integer = random.randint(1, 10)
# print(random_integer)
# print(my_module.pi)
#
# random_float = random.random()
# print(random_float)
#
# # Heads or Tails
# # coin = round(random.random())
# coin = random.randint(0, 1)
# print(coin)
# if coin == 1:
#     print("Heads")
# else:
#     print("Tails")

# # Lists
# states_of_america = ["Delaware", "Pennsylvania"]
# states_of_america[1] = "New-Pennsylvania"
# states_of_america.append("Angela land")
# # states_of_america[3] = "GM Land" ! IndexError: list assignment index out of range
# print(states_of_america)
# states_of_america.extend(["GM Land", "Jack Bauer Land"])
# print(states_of_america)

# # Random choice
# li = [1, 2, 3, 4]
# print(random.choice(li))

# #  Banker Roulette
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# print(names)
# print(f"{names[randint(0, len(names) - 1)]} is going to buy the meal today!")

# # Treasure Map
#
#
# row1 = ["⬜️", "️⬜️", "️⬜️"]
# row2 = ["⬜️", "⬜️", "️⬜️"]
# row3 = ["⬜️️", "⬜️️", "⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# map[int(position[1]) - 1][int(position[0]) - 1] = "X"
# print(f"{row1}\n{row2}\n{row3}")

# rock-paper-scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
'''
MY METHOD
# choice = [rock, paper, scissors][int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors"))]
# print(choice)
# pc_choice = [rock, paper, scissors][random.randint(0, 2)]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")

if computer_choice - user_choice == 1 or computer_choice - user_choice == -2:
    print("You loose")
elif computer_choice - user_choice == -1 or computer_choice - user_choice == 2:
    print("You win")
elif computer_choice == user_choice:
    print("There is draw")
'''

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you loose!")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print(game_images[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You loose")
    elif computer_choice > user_choice:
        print("You loose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
