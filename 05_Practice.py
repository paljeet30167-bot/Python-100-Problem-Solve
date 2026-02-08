import os
os.system("cls")

"""Write a Python Program to Take a number from user and print its table"""

# user input (num), i = 1 to 10, 
num = int(input("ENter the number which table you want:"))

for i in range(1,11):
    pahada = num*i
    print(pahada)