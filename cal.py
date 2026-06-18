'''
     Simple Calculator in python
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division  
'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sign = input("Enter the operation you want to perform: ")
if sign == "+":
    print(num1 + num2)
elif sign == "-":
    print(num1 - num2)
elif sign == "*":
    print(num1 * num2)
elif sign == "/":
    print(num1 / num2)
else:
    print("Invalid operation")
    