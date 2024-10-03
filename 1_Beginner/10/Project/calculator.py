# import logo from art.py
from art import logo

# operations
def add(num1, num2):
    return num1+num2

def subtract(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    return num1/num2

# dictionaries can be used to store functions with the same parameter amount
operations = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}

# initialization
num1 = 0
num2 = 0
first_exists = False
print(logo)
while True:
    if not first_exists:
        num1 = float(input("What's the first number?\n>> "))
    first_exists = False
    for k in operations.keys():
        print(k)
    operation_symbol = input("Choose the operation (+|-|*|/)!\n>> ")
    if operation_symbol not in ["+","-","*","/"]:
        print("Wrong operation symbol!")
        input("Press enter to continue..")
        continue
    num2 = float(input("What's the second number?\n>> "))
    result = operations[operation_symbol](num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    if input(f"Type 'y' to continue calculating with {result}, or type 'n' if you want to start new calculation!\n>>") =='y':
        num1 = result
        first_exists = True