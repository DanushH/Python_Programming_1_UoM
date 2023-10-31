import math

history_list = []

# TODO: Write the functions for arithmatic operations here
# These functions should cover Task 2
def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    try:
        return number1 / number2
    except Exception as e:
        print(e)

def power(number1, number2):
    return math.pow(number1, number2)


def remainder(number1, number2):
    return number1 % number2


def history(history_list):
    if not history_list:
        print("No past calculations to show")
    else:
        for i in history_list:
            print(i)   
    

# -------------------------------------
# TODO: Write the select_op(choice) function here
# This function sould cover Task 1 (Section 2) and Task 3
def select_op(choice):

    if choice == "#":
        return -1
    
    elif choice.endswith('$'):
        # print("Resetting")
        return 0

    elif choice not in "+-*/^%?":
        # print("Unrecognized operation")
        return 0
    
    elif choice in "+-*/^%":
        while (True):
            num1s = str(input("Enter first number: "))
            print(num1s)
            if num1s.endswith('$'):
                return 0
            if num1s.endswith('#'):
                return -1
            
            try:
                num1 = float(num1s)
                break
            except:
                print("Not a valid number,please enter again")
                continue
            
        while (True):
            num2s = str(input("Enter second number: "))
            print(num2s)
            if num2s.endswith('$'):
                return 0
            if num2s.endswith('#'):
                return -1
            try:  
                num2 = float(num2s)
                break
            except:
                print("Not a valid number,please enter again")
                continue
            
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
        
        output = f"{num1} {choice} {num2} = {answer}"
        print(output)
        history_list.append(output)

    elif choice == '?':
        history(history_list)
    
    
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
    print("8.History  : ? ")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
    print(choice)

    if select_op(choice) == -1:
        # program ends here
        print("Done. Terminating")
        exit()
