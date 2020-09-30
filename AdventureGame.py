import time
import random

print("what is your name, traveller?")

name = input()

while name == "":
    print("Please enter your name.")
    name = input()
print("Welcome, brave " + name + ", to your first grand adventure!")

time.sleep(1)

print("Walking down the road to Northshire, you come across an giant snail attacking a merchant and his overturned wagon")
time.sleep(1)
print("What type of combat do you specialize in?")
time.sleep(1)
print("Melee")
time.sleep(1)
print("Ranged")
time.sleep(1)
print("Magic")
weaponType = input()

while weaponType.lower() not in ["melee", "ranged", "magic"]:
        print("Please choose your combat specialization.")
        weaponType = input()
if weaponType.lower() == "melee":
    print("You unsheathe your trusty sword and charge towards the beast!")
elif weaponType.lower() == "ranged":
    print("You nock an arrow and take aim at the beast!")
elif weaponType.lower() == "magic":
    print("You concentrate and feel lightning dance between your fingertips as you look towards the beast!")
time.sleep(1)
print("The snail moves slowly towards you")