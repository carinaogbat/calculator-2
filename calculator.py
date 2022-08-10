"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True: #repeat forever
    calculation_chosen = input("Please type equation here (+ - * / square cube pow mod)") # read input
    tokens = calculation_chosen.split(' ') # tokenize input
    num1 = tokens[1]
    if tokens[2] is True:
        num2 = tokens[2]
    # # num3 = tokens[3]
    
    if tokens[0] == "q":
        print("You have quit the calculator, goodbye.")
        break

    elif tokens[0] == "+":
        result = add(float(num1), float(num2))
        

    elif tokens[0] == "-":
        result = subtract(float(num1), float(num2))

    elif tokens[0] == "*":
        result = multiply(float(num1), float(num2))

    elif tokens[0] == "/":
        result = divide(float(num1), float(num2))

    elif tokens[0] == "square":
        result = square(float(num1))

    elif tokens[0] == "cube":
        result = cube(float(num1))

    elif tokens[0] == "pow":
        result = power(float(num1), float(num2))

    elif tokens[0] == "mod":
        result = mod(float(num1), float(num2))

    # elif tokens[0] == "x+":
    #     result = add_mult(num1, num2, num3)

    # elif tokens[0] == "cubes+":
    #     result = add_cubes(num1, num2)

    else:
        result = "Please enter an operator followed by two integers."
    
    print(result)
