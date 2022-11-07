# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

#     def first_odds():
#         .....

def first_odds():
    for number in range(1, 101):
        if(number % 2 != 0):
            print(number)            
first_odds()