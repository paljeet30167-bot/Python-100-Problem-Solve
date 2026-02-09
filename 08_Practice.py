"""Write a Python program to Accept a year and check if it a leap year  or not"""
year = int(input("Enter the Year :"))

if year % 100 == 0 and year % 400:
    print("its a leap year")
elif year % 100 != 0 or year % 4 == 0:
    print("its a leap year")
else:
    print("Its a Normal year")