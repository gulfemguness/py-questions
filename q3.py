# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

#     def max_num_in_list(a_list):
#         .....


def max_num_in_list(a_list):
    num = a_list[0]
    for max_num in a_list:
        if max_num > num:
            return max(a_list)
# a_list = [4, 5, 2, -6, 0, 18]
a_list = [99, 389, 2, 1, 0, -56, -7]
print(max_num_in_list(a_list))  