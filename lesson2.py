'''
Name: Peter V.
Date: 9/24/24
Description: More on f-strings, input and number/ops
'''

print("Hello chat")

my_int = 5
my_float = 3.15
my_bool = True
print(f"{my_int} {my_float} {my_bool}")

another_float = 8.0 # make this a float by adding .0
float_part_two = float(8) # or cast
print(f"{another_float} {float_part_two}")

# get decimal from user
# radius = float(input("Enter a radius: "))

# operations on numbers
# P E MModD AS
# remainder operation %
print(15 % 7) # prints the remainder of 15/7

# exponent is not ^, it's **
print(5**1249)

# odd math things
print(0.3 - 0.2)
print(round(0.3 - 0.2, 2))

# your turn to code
# ask a user for some amount of dollars
# Convert that money to some currency of your choice
# Store the conversion factor in a variable
# Store the final amount in a variable
# Print it like "___ USD is the same as ___ [Currency]". Round to two decimal places

dollar = round(float(input("Enter how much money you have: ")))
conversion_factor = 83.64 # as of right now
Indian_Rupee = dollar * conversion_factor

print(f"{dollar} USD is {Indian_Rupee} Indian Rupees as of right now")