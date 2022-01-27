# Define a function named is_two. It should accept one input and return True 
# if the passed input is either the number or the string 2, False otherwise.
def is_two(i):
    if type(i) == int or i == '2' :
        return True
    else:
        return False

# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(i):
    if i.lower() in 'aeiou':
        return True
    else:
        return False

is_vowel('p')

# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.
def is_consonant(str):
    if str not in 'aeiou':
        return True
    else:
        return False

is_consonant('')

# Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.
def capit(str):
    if str[0] not in 'aeiou':
        capitalized = str[0].upper() + str[1:]
        print(capitalized)
    else:
        return False


def capit(str):
    'using capitalize function'
    if str[0] not in 'aeiou':
        return str.capitalize()

# Define a function named calculate_tip. 
# It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(tip_per, total):
    if tip_per > 0 or tip_per < 1:
        tip_amount = tip_per * total
        return tip_amount
        print (tip_amount)

calculate_tip(0.15, 15)


# Define a function named apply_discount. It should accept a original price, and a discount percentage,
#  and return the price after the discount is applied.
def apply_discount(orgprice, disc):
    disc_amount = (orgprice * disc) 
    new_price = orgprice - disc_amount
    return new_price
    print (new_price)

apply_discount(10, 0.15)


# Define a function named handle_commas. It should accept a string that is a number 
# that contains commas in it as input, and return a number as output.
def handle_commas(str):
    new_str = []
    for i in str:
        if i == ',' or i == '$':
            continue
        else:
            new_str.append(i)
    num_wo_commas = float(''.join(new_str))
    return (num_wo_commas)
        
handle_commas('1,000,000.01')


# Define a function named get_letter_grade. 
# It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(num):
    if num in range(90, 100):
        return 'A'
        print ('A')
    elif num in range(80, 90):
        return 'B'
        print ('B')
    elif num in range(70, 80):
        return 'C'
        print ('C')
    elif num in range(60, 70):
        return 'D'
        print ('D')
    else:
        return 'F'
        print ('F')

get_letter_grade(90)


# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(str):
    new_list = []
    for i in str:
        if i in 'aeiou':
            continue
        else:
            new_list.append(i)
    new_str = ''.join(new_list)
    print(new_str)

remove_vowels('concatenation')

# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed
def normalize_name(str):
    new_str = []
    for i in str:
        if i == ' ':
            new_str.append('_')
        else:
            new_str.append(i)
    new_str1 = ''.join(new_str)
    new_str2 = new_str1.strip().lower()
    print(new_str2)

normalize_name('Jay Choi')



# Write a function named cumulative_sum that accepts a list of numbers and 
# returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
def cumulative_sum(nums):
    cum_list = []
    x = 0
    for i in nums:
        x += i
        cum_list.append(x)
        
    return cum_list
    print(cum_list)

cumulative_sum([1, 2, 3, 4])



# Additional Exercise
# Once you've completed the above exercises, 
# follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 
# in order to thouroughly comment your code to explain your code.

# Bonus
# Create a function named twelveto24. It should accept a string 
# in the format 10:45am or 4:30pm and return a string 
# that is the representation of the time in a 24-hour format.


#  Bonus write a function that does the opposite.
# Create a function named col_index. It should accept a spreadsheet column name, 
# and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27