import math


# TODO: Write the functions for arithmatic operations here
# These functions should cover Task 2
def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    if number2 == 0:
        print("float division by zero")
        return "None"
    else:
        return round((number1 / number2), 1)


def power(number1, number2):
    return math.pow(number1, number2)


def remainder(number1, number2):
    return number1 % number2


# -------------------------------------
# TODO: Write the select_op(choice) function here
# This function sould cover Task 1 (Section 2) and Task 3
def select_op(choice):
    if choice == "#":
        return -1
    
    elif choice.endswith('$'):
        # print("Resetting")
        return 0

    elif choice not in "+-*/^%":
        # print("Unrecognized operation")
        return 0
    
    elif choice in "+-*/^%":
        print("Enter first number: ", end = "")
        num1 = input()
        print(num1)

        if num1.endswith('$'):
            # print("Resetting")
            return 0
        if num1.endswith('#'):
            return -1
        if not(num1.isdigit()):
            # print("Not a valid number,please enter again")
            return 0
        
        print("Enter second number: ", end = "")
        num2 = input()
        print(num2)

        if num2.endswith('$'):
            # print("Resetting")
            return 0
        if num2.endswith('#'):
            return -1
        if not(num2.isdigit()):
            # print("Not a valid number,please enter again")
            return 0
        
        num1 = float(num1)
        num2 = float(num2)
            
        if choice == "+":
            answer = add(num1, num2)
        elif choice == "-":
            answer = subtract(num1, num2)
        elif choice == "*":
            answer = multiply(num1, num2)
        elif choice == "/":
            answer = divide(num1, num2)
        elif choice == "^":
            answer = power(num1, num2)
        elif choice == "%":
            answer = remainder(num1, num2)
        
        print(f"{num1} {choice} {num2} = {answer}")

    
# End the select_op(choice) function here
# -------------------------------------
# This is the main loop. It covers Task 1 (Section 1)
# YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)

    if select_op(choice) == -1:
        # program ends here
        print("Done. Terminating")
        exit()
