# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

#     def hello_name(user_name):
#         .....

def hello_name(user_name):
    user_name = input("Enter your username:")
    print("hello_" + user_name.upper() + "!")
hello_name(user_name=input)