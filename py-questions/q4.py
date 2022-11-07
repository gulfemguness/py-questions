# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

#     def is_leap_year(a_year):
#         .....
"""
    An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. 
    It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. 
    A leap year contains a leap day. In the Gregorian calendar, three conditions are used to identify leap years: 
    The year can be evenly divided by 4, is a leap year, unless: The year can be evenly divided by 100, 
    it is NOT a leap year, unless: The year is also evenly divisible by 400. Then it is a leap years. 
    Solution is the below Python Code.
"""

def is_leap(year):
  leap = False

  if (year % 4 == 0) and (year % 100 != 0): 
      leap = True
  elif (year % 100 == 0) and (year % 400 != 0):
      leap = False
  elif (year % 400 == 0):
      leap = True
  else:
      leap = False
  return leap

year = int() 
print(is_leap(year=2020))