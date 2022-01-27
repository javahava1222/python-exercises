# Conditional Basics

# prompt the user for a day of the week, print out whether the day is Monday or not

day_of_the_week = input('Please input a day of the week: ')
if day_of_the_week.lower() == 'monday':
    print (f"The day is {day_of_the_week}")
else:
    print ('The day is not Monday')

# prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day_of_the_week = input('Please input a day of the week: ')
if day_of_the_week.lower() == 'saturday':
    print ('The day is weekend')
elif day_of_the_week.lower() == 'sunday':
    print ('The day is weekend')
else: 
    print ('The day is weekday')

# create variables and make up values for

# the number of hours worked in one week
hours_worked = 42
# the hourly rate
hourly_rate = 17
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half 
# if you work more than 40 hours

if hours_worked > 40:
    weekly_paycheck = (40 * hourly_rate) + ((hours_worked - 40) * (hourly_rate * 1.5))
    print(weekly_paycheck)
else: 
    weekly_paycheck = hours_worked * hourly_rate
    print(weekly_paycheck)

# Loop Basics

# While

# Create an integer variable i with a value of 5.

# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
# Your output should look like this:
i = 5
while i <= 15:
    print (i)
    i += 1

# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15



# Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.
i = 0
while i <= 100:
    print (i)
    i += 2
    
# Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i -= 5

# Create a while loop that starts at 2, 
# and displays the number squared on each line while the number is less than 1,000,000.
#  Output should equal:
i = 2
while i < 1000000:
    print(i)
    i = i**2
#  2
#  4
#  16
#  256
#  65536


# Write a loop that uses print to create the output shown below.
i = 100
while i >= 5:
    print(i)
    i -= 5

# 100
# 95
# 90
# 85
# 80
# 75
# 70
# 65
# 60
# 55
# 50
# 45
# 40
# 35
# 30
# 25
# 20
# 15
# 10
# 5

# For Loops

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

# For example, if the user enters 7, your program should output:
number = ''
while number not in range(1,11):
    number = int(input('Please input a number from 1 to 10 for which you want to see a multiplication table'))

for i in range(1,11):
    print(number, 'x', i, '=', number * i) 

#alternate solution
user_number = input('Please input number')


# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70


# Create a for loop that uses print to create the output shown below.
for x in range(1,10):
    num_list = ([x] * x)
    str_int = (str(i) for i in num_list)
    new_num = ''.join(str_int)
    print(new_num)
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999


# break and continue
# Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
# except for the number the user entered.
odd_num = ''

while (odd_num not in range(1,51,2)):
    odd_num = int(input('Select an odd number between 1 and 50'))
    for odd_num1 in range(1,51,2):
        if odd_num1 != odd_num:
            print(f'Here is an odd number: {odd_num1}')
        else:
            print(f'Yikes! Skipping number: {odd_num}')



# Your output should look like this:


# Number to skip is: 27

# Here is an odd number: 1
# Here is an odd number: 3
# Here is an odd number: 5
# Here is an odd number: 7
# Here is an odd number: 9
# Here is an odd number: 11
# Here is an odd number: 13
# Here is an odd number: 15
# Here is an odd number: 17
# Here is an odd number: 19
# Here is an odd number: 21
# Here is an odd number: 23
# Here is an odd number: 25
# Yikes! Skipping number: 27
# Here is an odd number: 29
# Here is an odd number: 31
# Here is an odd number: 33
# Here is an odd number: 35
# Here is an odd number: 37
# Here is an odd number: 39
# Here is an odd number: 41
# Here is an odd number: 43
# Here is an odd number: 45
# Here is an odd number: 47
# Here is an odd number: 49


# The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 

x = int(input('Please input postive number'))
while x < 0:
    x = input('Please write positive number')
for num in range(0,x+1):
    print(num)
    

# (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, so you'll need to convert this to a numeric type.)

# Write a program that prompts the user for a positive integer.
#  Next write a loop that prints out the numbers from the number the user entered down to 1.
x = int(input('Please input postive number'))
while x < 0:
    x = input('Please write positive number')
for num in range(0,x+1):
    print(num)



# Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
# Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
# Example Output


# What number would you like to go up to? 5

# Here is your table!

# number | squared | cubed
# ------ | ------- | -----
# 1      | 1       | 1
# 2      | 4       | 8
# 3      | 9       | 27
# 4      | 16      | 64
# 5      | 25      | 125
# Bonus: Research python's format string specifiers to align the table

# Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0
# Bonus

# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
# Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.

# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.