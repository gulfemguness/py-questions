# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

#     def is_consecutive(a_list):
#         .....

my_list = [2,3,9,0,-1,4,5,6,7]
my_list2 = [1,2,4,5]

# a_list[0]=2
# a_list[1]=3 
# a_list[2]=4

def is_consecutive(a_list):
    length = len(a_list)
    i = 0
   
    while i < length-1:
        if a_list[i+1] - a_list[i] == 1:
            i += 1
            result = True
        else:
            result = False
            break 
    print(result)

is_consecutive(my_list)
