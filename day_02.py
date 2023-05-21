print(type(len("Hello")))
# Data Types
# Subscripting
print("Hello"[0])
print("Hello"[0:2])
# Integer
large_num = 120_000
# Float
PI = 3.1415
print(type(PI))
a = float(123)
print(a)
"""
two_digit_num = input("enter two digit number ")
print(int(two_digit_num[0]) + int(two_digit_num[1]))
"""
print(6 / 3)
# PEMDAS order
#  P- Parentheses, E- Exponents, M- Multiplication, D- Division, A- Addition, and S- Subtraction
print(3 * (3 + 3) / 3 - 3)
"""
# BMI
weight = input("Enter your weight: ")
height = input("Enter your height: ")
bmi = float(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)
"""
print(round(8 / 3, 2))
print(round(2.666666666666, 2))
# floor division // rounds the result down to the nearest whole number
print(8 // 3)
# f-String
score = 1
isWinning = True
print(f"your score is {score}, you are winning is {isWinning}")
"""
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
years_remaining = 90 - int(age)
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)
"""
print(6 + 4 / 2 - (1 * 2))

# Tip Calculator
print("Welcome to tip calculator")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15 ? "))
people = int(input("How many people to split the bill? "))
total_bill = bill + bill * tip / 100
# total_bill = bill * (1 + tip / 100)
# each_pays = round(total_bill / people, 2)
each_pays = "{:.2f}".format(total_bill / people, 2)
print(f"Each person should pay: ${each_pays}")
