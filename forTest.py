import random

a = 79
print(a // 10)

# choice = [rock, paper, scissors][int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors"))]
# print(choice)
# pc_choice = [rock, paper, scissors][random.randint(0, 2)]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you loose!")
elif computer_choice - user_choice == 1 or computer_choice - user_choice == -2:
    print("You loose")
elif computer_choice - user_choice == -1 or computer_choice - user_choice == 2:
    print("You win")
elif computer_choice == user_choice:
    print("There is draw")
