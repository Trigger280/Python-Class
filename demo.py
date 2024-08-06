def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Test the functions with integers and floats
num1 = 10
num2 = 5
num3 = 7.5
num4 = 2.5

print(f"Addition of {num1} and {num2}: {add(num1, num2)}")
print(f"Subtraction of {num2} from {num1}: {subtract(num1, num2)}")
print(f"Multiplication of {num1} and {num2}: {multiply(num1, num2)}")
print(f"Division of {num1} by {num2}: {divide(num1, num2)}")

print(f"Addition of {num3} and {num4}: {add(num3, num4)}")
print(f"Subtraction of {num4} from {num3}: {subtract(num3, num4)}")
print(f"Multiplication of {num3} and {num4}: {multiply(num3, num4)}")
print(f"Division of {num3} by {num4}: {divide(num3, num4)}")

# Mixing integers and floats
print(f"Addition of {num1} and {num4}: {add(num1, num4)}")
print(f"Subtraction of {num4} from {num1}: {subtract(num1, num4)}")
print(f"Multiplication of {num1} and {num4}: {multiply(num1, num4)}")
print(f"Division of {num1} by {num4}: {divide(num1, num4)}")
