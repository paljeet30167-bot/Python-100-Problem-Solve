"""Write a Python Program to Aceept two numbers and print the greatest between them."""

num1 = int(input("Enter the number1 :"))
num2 = int(input("Enter the number2 :"))

if num1 > num2:
    print(f"{num1} is greater then {num2}")  
else:
    print(f"{num2} is greater then {num1}")