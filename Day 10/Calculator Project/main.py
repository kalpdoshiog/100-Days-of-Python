from art import logo
print(logo)
# TODO: Write out the other 3 functions - addition, subtract, multiply and divide.

def add(n1, n2):
    """It takes two variables in number datatype and performs an addition operation."""
    return n1 + n2

def sub(n1, n2):
    """It takes two variables in number datatype and performs a subtraction operation."""
    return  n1 - n2

def mul(n1, n2):
    """It takes two variables in number datatype and performs a multiplication operation."""
    return  n1 * n2

def div(n1, n2):
    """It takes two variables in number datatype and performs a division operation."""
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}
# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
# multiplication = 4 * 8

# multiplication = operations["*"](4, 8)
# print(multiplication)

# Program asks the user to type the first number.
# first_num = int(input("What is the first number? "))
# Program asks the user to type a mathematical operator (a choice of "+", "-", "*" or "/")
# operation = input("Which mathematical operation you wanna perform? \n + \n - \n * \n / \n Please enter mathematical operator ")

# Program asks the user to type the second number.
# second_num = int(input("What is the second number? "))

def calc(first_num, second_num, operation):
    # Program works out the result based on the chosen mathematical operator.
    result = operations[operation](first_num,second_num)
    print(f"The result is: {result}")
    return result

should_restart = True
while should_restart:
    first_num = int(input("What is the first number? "))
    keep_going = True
    while keep_going:
        operation = input("Which mathematical operation you wanna perform? \n + \n - \n * \n / \n Please enter mathematical operator ")
        second_num = int(input("What is the second number? "))
        result = calc(first_num,second_num, operation)

        more_calc = input(f"If you want to continue press 'y' or 'n' to start the new calculation")

        if more_calc == 'y':
            first_num = result
        else:
            keep_going =False
            print("\n" * 20 )

    # if operation == "+":
    #     result = operations["+"](first_num, second_num)
    #     print(result)
    # elif operation == "-":
    #     result = operations["-"](first_num,second_num)
    #     print(result)
    # elif operation == "*":
    #     result = operations["*"](first_num,second_num)
    #     print(result)
    # elif operation == "/":
    #     result = operations["/"](first_num,second_num)
    #     print(result)

# more_calc = input(f"If you want to continue press 'y' or 'n' to start the new calculation")
#
# if more_calc == "y":
#     new_second_num = int(input("What is the second number? "))
#     def more_calculation(result, new_second_num):
#         operation = input("Which mathematical operation you wanna perform? \n + \n - \n * \n / \n Please enter mathematical operator ")
#         if operation == "+":
#             new_result = operations["+"](result, new_second_num)
#             print(new_result)
#         elif operation == "-":
#             new_result = operations["-"](result, new_second_num)
#             print(new_result)
#         elif operation == "*":
#             new_result = operations["*"](result, new_second_num)
#             print(new_result)
#         elif operation == "/":
#             new_result = operations["/"](result, new_second_num)
#             print(new_result)
#         more_calculation(result, new_second_num)
# elif more_calc == "n":
#     print("\n" * 20)
#     calc(first_num,second_num)


# calc(first_num,second_num, operation)
# Program asks if the user wants to continue working with the previous result.



