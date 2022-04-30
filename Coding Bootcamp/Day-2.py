#Data Types

# Strings
print('Hello'[4])

# Integers - Whole numbers either positive or negative are called integers
print(123456 + 345678)
# The integers can be seperated with an _ to represent a , in the human notation of a number
print(123_456 + 345_678)

# Float - A floating point number is a number with a floating point (.) within it, i.e a decimal number
floatNumber = 12.345

# Boolean
condition1 = True
condition2 = False

# Data casting/conversion
# types
a = '123'
type(a) #str

b = 123
type(b) #int

# no_of_char = str(len(input('What is your name?\n')))
# print('Your name has ' + no_of_char + ' characters.')


# Mathematical Operations ORDER OF PRIORITY - BEDMAS taking a priority from left to right
a = 6 + 4 #Addition
b = 6 * 4 #multiplication
c = 6 / 2 #Division - a division operation always returns a float
d = 2 ** 3 #Exponentiation

# print(int(2.75)) #output 2 passing a float to an int function would take the whole number part of the float
# print(float(2)) #output 2.0 passing an int to a float function would take the whole number part and convert it to a float

# Number Manipulation and F strings
print(round(8/3, 2)) #rounds up the value to a specific number of decimal places, 0 by default

# Floor division
print(8 // 3) #takes the whole number part and converts it to an integer and not a floating point number

# f string
score = 12
print(f'your score is {score}') # basically a formatted string