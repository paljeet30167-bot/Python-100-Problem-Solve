import os
os.system("cls")

gender = input("Enter the Gender :")  #take input from the user
 
if gender == "M" or gender == "m":
    print("Good Morning Sir")  
elif gender == "F" or gender == "f":
    print("Good Morning Ma'am")
else:
    print("unidentifies")