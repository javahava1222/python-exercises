# Import and test 3 of the functions from your functions exercise file. Import each function in a different way:
from audioop import avg
import function_exercises as f_e

# Run an interactive python session and import the module. Call the is_vowel function using the . syntax.
f_e.is_vowel('a')

# Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly.
#  Call this function with values you choose and print the result.
from function_exercises import calculate_tip
calculate_tip(0.15, 10)

# Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade function and give it an alias. 
# Test this function in your notebook.
# Make sure your code that tests the function imports is run from the same directory that your functions exercise file is in.

# Read about and use the itertools module from the python standard library to help you solve the following problems:

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
import itertools
itertools.combinations(range(1,4),'abc')

# How many different combinations are there of 2 letters from "abcd"?
itertools.combinations('abcd', 2)

# How many different permutations are there of 2 letters from "abcd"?
itertools.permutations('abcd', 2)

# Save this file as profiles.json inside of your exercises directory (right click -> save file as...).

# Use the load function from the json module to open this file.
import json

json.load(open('profiles.json'))


# import json

# json.load(open('profiles.json'))
# Your code should produce a list of dictionaries. 
# Using this data, write some code that calculates and outputs the following information:

# Total number of users -- 19
a = 0
for i in json.load(open('profiles.json')):
    a += 1
print(a)

# Number of active users -- 9
a = 0
for i in json.load(open('profiles.json')):
    if i['isActive'] == True:
        a += 1
print(a)
# Number of inactive users -- 10 
a = 0
for i in json.load(open('profiles.json')):
    if i['isActive'] == False:
        a += 1
print(a)
# Grand total of balances for all users -- 52667.02
from function_exercises import handle_commas
ls = []
for i in json.load(open('profiles.json')):
    ls.append(handle_commas(i['balance']))

l_sum = sum(ls)
print(l)

# Average balance per user -- 2771.95
l1 = l_sum/len(ls)
print(l1)
# User with the lowest balance -- 1214.1 -- Avery Flynn
l2 = min(ls)
print(l2)
# or 
for i in json.load(open('profiles.json')):
    if i['balance'] == '$1,214.10':
        user_name = i['name']
        print(user_name)

# User with the highest balance -- 3919.64 -- Fay Hammond
l3 = max(ls)
print(l3)

for i in json.load(open('profiles.json')):
    if i['balance'] == '$3,919.64':
        user_name = i['name']
        print(user_name)

# Most common favorite fruit -- strawberry
def mostcommonFruit(lst):
    return max(set(lst), key=lst.count)
    
list1 = []
for i in json.load(open('profiles.json')):
    list1.append(i['favoriteFruit'])

mostcommonFruit(list1)

# Least most common favorite fruit -- apple
def leastcommonFruit(lst):
    return min(set(lst), key=lst.count)

leastcommonFruit(list1)

# Total number of unread messages for all users
lst = []
for i in json.load(open('profiles.json')):
    for j in i['greeting']:
        if type(j) == int:
            lst.append(j)

total = sum(lst)
print(total)
