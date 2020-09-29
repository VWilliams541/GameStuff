import time
import random

print("what is your name, traveller?")

name = input()

while name == "":
    print("Please enter your name.")
    name = ""
print("Welcome brave " + name + " to your first grand adventure!")
