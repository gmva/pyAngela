print("Starting")

# print("Welcome to rollercoaster!")
# height = int(input("enter your height "))
# bill = 0
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7")
#     elif 45 <= age <= 55:
#         print("You can ride for free")
#
#     else:
#         bill = 12
#         print("Adult tickets are $12")
#     wants_photo = input("Do you want a photo taken Y or N.? ")
#     if wants_photo == "Y":
#         bill += 3
#     print(f"Your final bill ${bill}")
#
# else:
#     print("Sorry you have to grow taller")

# num = int(input("Enter integer "))
# if num == 5:
#     print("you entered 5")
# else:
#     print("you entered something else")

# odd or even
# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# # BMI 2.0
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# bmi = round(weight / height ** 2)
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")

# # Leap year
# year = int(input("Please enter a year "))
# if year % 4 == 0:
#     if year % 100 != 100:
#         print(f"{year} i a leap year")
#     elif year % 400 == 0:
#         print(f"{year} i a leap year")
# else:
#     print(f"{year} i NOT a leap year")

# # Pizza Order
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0
# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# elif size == "L":
#     bill = 25
# if extra_cheese == "Y":
#     bill += 1
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     elif size == "M" or size == "L":
#         bill += 3
# print(f"Your final bill is: ${bill}")

# a = 12
# print(not a > 100)

# # Love Calculator
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# tg_lower = (name1 + name2).lower()
# t = tg_lower.count("t")
# r = tg_lower.count("r")
# u = tg_lower.count("u")
# e = tg_lower.count("e")
# true = t + r + u + e
# l = tg_lower.count("l")
# o = tg_lower.count("o")
# v = tg_lower.count("v")
# # e = tg_lower.count("e")
# love = l + o + v + e
# love_score = int(str(true) + str(love))
# print(love_score, type(love_score))
# # we can use parentheses if we want
# if (love_score < 10) or (love_score > 90):
#     print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif 40 < love_score < 50:
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#     print(f"Your score is {love_score}.")

# Treasure island
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("left or right? ").lower()
if direction == "left":
    swim_or_wait = input("Swim or wait? ").lower()
    if swim_or_wait == "wait":
        door = input("Which door Red, Blue or Yellow? ").lower()
        if door == "yellow":
            print('''
            YOU WIN
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
            ''')
        else:
            print("Game Over!")
    else:
        print("Game Over!")

else:
    print("Game Over!")
