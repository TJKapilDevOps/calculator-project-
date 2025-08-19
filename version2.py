
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return n1 / n2

# Dictionary:

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
while True:
    try:
        first_number = float(input("What's the first number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    next_Part = True
    while next_Part:

        operation = float('Pick an operation ( +  -  *  /): ').strip()
        if operation not in operations:
            print("Please enter a valid operation.")
            continue
        try:
            second_number = float(input('Enter second number: '))
            result = operations[operation](first_number, second_number)
        except ValueError:
            print("Please enter a valid number.")
            continue
        except ZeroDivisionError as e:
            print(e)
            continue
        print(f"{first_number} {operation} {second_number} = {result}")
        nextStep = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if nextStep == 'y':
            first_number = result
        elif nextStep == 'n':
            next_Part = False
        else:
            print("Invalid input. Please try again.")


