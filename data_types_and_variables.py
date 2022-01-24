# You have rented some movies for your kids: The little mermaid (for 3 days),
# Brother Bear (for 5 days, they love it), and Hercules (
# 1 day, you don't know yet if they're going to like it).
# If price for a movie per day is 3 dollars, how much will you have to pay?
little_mermaid_price = 3 * 3
brother_bear_price = 5 * 3
hercules_price = 1 * 3

total_price = little_mermaid_price + brother_bear_price + hercules_price
print (total_price)


# Suppose you're working as a contractor for 3 companies:
#  Google, Amazon and Facebook, they pay you a different rate per hour.
#  Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
facebook = 350 * 10
google = 400 * 6
amazon = 380 * 4

total_pay = facebook + google + amazon
print (total_pay)

# A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.
class_room_available = True
schedule_is_available = False
enrollment = class_room_available AND schedule_is_available
print (f'Can student enrolle in the class? \n {enrollment}')

# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.
is_premium_member = True
purchase_more_than_two = False
offer_not_expired = True
discount_valid = offer_not_expired and (is_premium_member or purchase_more_than_two)


# Continue working in your data_types_and_variables.py file. 
# Use the following code to follow the instructions below:
username = 'codeup'
password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:


# the password must be at least 5 characters
password_meets_length_req = len(password) >= 5
# the username must be no more than 20 characters
username_meet_length_req = len(username) <= 20
# the password must not be the same as the username
password_not_equal_to_password = username != password
# bonus neither the username or password can start or end with whitespace
username_has_spaces = username != username.strip()
username_has_spaces = password != password.strip()
