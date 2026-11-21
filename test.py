
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."


try:
    num1=int(input("Enter the first number: "))
    op=input("Enter the operator (+, -, *, /): ")
    num2=int(input("Enter the second number: "))
except ValueError:
    print("Error: Please enter valid numbers.")
    exit()

if op == "+":
    result = add(num1, num2)
elif op == "-":
    result = subtract(num1, num2)
elif op == "*":
    result = multiply(num1, num2)
elif op == "/":     
    result = divide(num1, num2)
else:
    print("Invalid operator. Please use +, -, *, or /.")
if result == "Error: Division by zero is not allowed.":
    print("Error: Division by zero is not allowed.")
else:
    print("The result of ",num1," ",op," ",num2," is: ",result)

    
