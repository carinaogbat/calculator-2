"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True: #repeat forever
    calculation_chosen = input("Please type equation here (+ - * / square cube pow mod)") # read input
    tokens = calculation_chosen.split(' ') # tokenize input
    
    # # num3 = tokens[3]

    if len(tokens) > 1:
        num1 = tokens[1]
    
    if len(tokens) > 2:
        num2 = tokens[2]

    
    if tokens[0] == "q":
        print("You have quit the calculator, goodbye.")
        break

    elif tokens[0] == "+":
        if num1.isdigit() and num2.isdigit():
            result = add(float(num1), float(num2))
        else:
            result = "Sorry, that was not a digit please try again."
        

    elif tokens[0] == "-":
        if num1.isdigit() and num2.isdigit():
            result = subtract(float(num1), float(num2))
        else:
            result = "Sorry, that was not a digit please try again."

    elif tokens[0] == "*":
        if num1.isdigit() and num2.isdigit():
            result = multiply(float(num1), float(num2))
        else:
            result = "Sorry, that was not a digit please try again."
        

    elif tokens[0] == "/":
        if num1.isdigit() and num2.isdigit():
            result = divide(float(num1), float(num2))
        else:
            result = "Sorry, that was not a digit please try again."
        

    elif tokens[0] == "square":
        if num1.isdigit() and num2.isdigit():
            result = square(float(num1))
        else:
            result = "Sorry, that was not a digit please try again."

    elif tokens[0] == "cube":
        if num1.isdigit() and num2.isdigit():
            result = cube(float(num1))
        else:
            result = "Sorry, that was not a digit please try again."

    elif tokens[0] == "pow":
        if num1.isdigit() and num2.isdigit():
            result = pow(float(num1), float(num2))
        else:
            result = "Sorry, that was not a digit please try again."
        

    elif tokens[0] == "mod":
        if num1.isdigit() and num2.isdigit():
            result = mod(float(num1), float(num2))
        else:
            result = "Sorry, that was not a digit please try again."

    # elif tokens[0] == "x+":
    #     result = add_mult(num1, num2, num3)

    # elif tokens[0] == "cubes+":
    #     result = add_cubes(num1, num2)

    else:
        result = "Please enter an operator followed by two integers."
    
    print(result)
