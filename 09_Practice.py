"""You can create if elif ladder using multiple condition of elif 
take the input of temperature in celsius"""
import os
os.system("cls")


tem = int(input("Enter the temprature : "))

if tem < 0:
    print("Its Cold")
elif tem >= 0 and tem < 10: 
    print("Very Cold")
elif tem >= 10 and tem < 20:
    print("Cold")
elif tem >= 20 and tem < 30:
    print("Its Pleasant")
elif tem >= 30 and tem < 40:
    print("its Hot")
else:
    print("its a Very hot")          