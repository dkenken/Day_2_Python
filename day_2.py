# Exercises Day #2

# Data Types (Strings, Interger, Float, Boolean)

# String
print("Hello Github")

# Interger
print(123 + 765)

# Float 
print(765.87)

print('')

#Boolean
True or False

print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')

# Write a program that adds the digits in a 3 digit number. e.g. if the input was 351, then the output should be 3 + 5 + 1 = 9
three_digit_number = input('Type a three digit number: ')

first_digit_number = three_digit_number[0]
second_digit_number = three_digit_number[1]
third_digit_number = three_digit_number[2]

result = int(first_digit_number) + int(second_digit_number) + int(third_digit_number)

print(result)

print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n')

# Mathematical Operations in Python

3 + 8  #Addition
8 - 4 #Sustraction
8 * 7 #Multiplication
8 / 4 #Division
9 // 2 #Floor
9 % 3 #Modulo
2 ** 3 #Exponentiator

#PEMDAS = () ** * / + - 

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

num_height = float(height)
num_weight = int(weight)
BMI = int(num_weight / (num_height ** 2))
print(BMI)

#  Number Manipulation and F strings in Python

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
age = input("What is your current age? ")

num_age = int(age)
time_limit = 90
year_left = time_limit - num_age
day_year = year_left * 365
week_year = year_left * 52
month_year = year_left * 12

print(f"you have {day_year} days, {week_year} weeks, and {month_year} months left.")
 
# Create a program that calculates each person bill to iclude the tip.
print("Welcome to the Tip calculator.")
total_bill = input("What was the total of your bill? $")
total_bill_num = float(total_bill)
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
split_bill = input("How many people to split the bill? ")

split_bill = (total_bill_num / 7) * 1.12
print(f"Each person should pay: {split_bill :.2f}")