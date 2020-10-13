# Python Activtiy
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# import regular expression module
import re

# # Part A. starts_with_number
# Define a function starts_with_number(s) that takes a string and returns true
# if it starts with a number and false otherwise.
# (For our purposes, a number is any character that is 0,1,2,3,4,5,6,7,8, or 9.)
def starts_with_number(s):
  startnum = False

  if s.startswith('1'):
    startnum = True
    return startnum
  if s.startswith('2'):
    startnum = True
    return startnum
  if s.startswith('3'):
    startnum = True
    return startnum
  if s.startswith('4'):
    startnum = True
    return startnum
  if s.startswith('5'):
    startnum = True
    return startnum
  if s.startswith('6'):
    startnum = True
    return startnum
  if s.startswith('7'):
    startnum = True
    return startnum
  if s.startswith('8'):
    startnum = True
    return startnum
  if s.startswith('9'):
    startnum = True
    return startnum
  if s.startswith('0'):
    startnum = True
    return startnum

  return startnum

# # Part B. starts_with_consonant
# Define a function starts_with_consonant(s) that takes a string and returns true
# if it starts with a consonant and false otherwise.
# (For our purposes, a consonant is any letter other than A, E, I, O, U.)
# Note: Be sure to use RegEx and it works for both upper and lower case and for nonletters!
def starts_with_consonant(s):
  startnum = False

  if s.startswith('b'):
    startnum = True
    return startnum
  if s.startswith('c'):
    startnum = True
    return startnum
  if s.startswith('d'):
    startnum = True
    return startnum
  if s.startswith('f'):
    startnum = True
    return startnum
  if s.startswith('g'):
    startnum = True
    return startnum
  if s.startswith('h'):
    startnum = True
    return startnum
  if s.startswith('j'):
    startnum = True
    return startnum
  if s.startswith('k'):
    startnum = True
    return startnum
  if s.startswith('l'):
    startnum = True
    return startnum
  if s.startswith('m'):
    startnum = True
    return startnum
  startnum = False
  if s.startswith('n'):
    startnum = True
    return startnum
  if s.startswith('p'):
    startnum = True
    return startnum
  if s.startswith('q'):
    startnum = True
    return startnum
  if s.startswith('r'):
    startnum = True
    return startnum
  if s.startswith('s'):
    startnum = True
    return startnum
  if s.startswith('t'):
    startnum = True
    return startnum
  if s.startswith('v'):
    startnum = True
    return startnum
  if s.startswith('w'):
    startnum = True
    return startnum
  if s.startswith('x'):
    startnum = True
    return startnum
  if s.startswith('y'):
    startnum = True
    return startnum
  if s.startswith('z'):
    startnum = True
    return startnum
  if s.startswith('B'):
    startnum = True
    return startnum
  if s.startswith('C'):
    startnum = True
    return startnum
  if s.startswith('D'):
    startnum = True
    return startnum
  if s.startswith('F'):
    startnum = True
    return startnum
  if s.startswith('G'):
    startnum = True
    return startnum
  if s.startswith('H'):
    startnum = True
    return startnum
  if s.startswith('J'):
    startnum = True
    return startnum
  if s.startswith('K'):
    startnum = True
    return startnum
  if s.startswith('L'):
    startnum = True
    return startnum
  if s.startswith('M'):
    startnum = True
    return startnum
  startnum = False
  if s.startswith('N'):
    startnum = True
    return startnum
  if s.startswith('P'):
    startnum = True
    return startnum
  if s.startswith('Q'):
    startnum = True
    return startnum
  if s.startswith('R'):
    startnum = True
    return startnum
  if s.startswith('S'):
    startnum = True
    return startnum
  if s.startswith('T'):
    startnum = True
    return startnum
  if s.startswith('V'):
    startnum = True
    return startnum
  if s.startswith('W'):
    startnum = True
    return startnum
  if s.startswith('x'):
    startnum = True
    return startnum
  if s.startswith('Y'):
    startnum = True
    return startnum
  if s.startswith('Z'):
    startnum = True
    return startnum

  return startnum


# Part C. binary_multiple_of_4
# define a method binary_multiple_of_4(s) that takes a string and returns true
# if the string represents a binary number that is a multiple of 4.
# Note: Be sure it returns false if the string is not a valid binary number!
# Hint: Use regular expressions to match for the pattern of a binary number that is a multiple of 4.
def binary_multiple_of_4(s):
  s = int(s)
  if s % 4 == 0:
    return True

  return False
