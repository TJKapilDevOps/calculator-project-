#-------------------------
# Functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return n1 / n2
#-----------------------------
def calculator(n1, n2, operation):
    if operation == "+":
        return add(n1, n2)
    elif operation == "-":
        return subtract(n1, n2)
    elif operation == "*":
        return multiply(n1, n2)
    elif operation == "/":
        return divide(n1, n2)
    else:
        raise ValueError("Invalid operation")
#-------------------------------
# User Input
while True:
    try:
        first_number = int(input("What's the first number?: "))
    except ValueError:
        print("Please enter a number.")
        continue
    nextStep = True

    while nextStep:

        operation = input("What's the operation: \n"
                          "* - + /\n")
        try:
            second_number = int(input("Whats the second number?: "))
            result = calculator(first_number, second_number, operation)
        except ValueError as e:
            print(e)
            continue
        except ZeroDivisionError as e:
            print(e)
            continue
        print(f"{first_number} {operation} {second_number} = {result}")

        nextValue = input(f"Type 'y' to continue calculating with "
                          f"{result}, "
                          f"or type 'n' to start a new calculation: ").lower()
        if nextValue == "y":
            first_number = result
        elif nextValue == "n":
            nextStep = False
        else:
            print("Invalid input. Try again.")




