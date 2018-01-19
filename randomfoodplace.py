import random

print("Hello there!\nI see you are trying to decide where to eat! Let me help you!")
print("Please name 5 places where you'd like to dine!")


myChoice1 = input()
myChoice2 = input()
myChoice3 = input()
myChoice4 = input()
myChoice5 = input()

decision = random.randint(1, 5)

if decision == 1:
    print ("Looks like you're eating at: " + myChoice1 + "!")
if decision == 2:
    print ("Looks like you're eating at: " + myChoice2 + "!")
if decision == 3:
    print ("Looks like you're eating at: " + myChoice3 + "!")
if decision == 4:
    print ("Looks like you're eating at: " + myChoice4 + "!")
if decision == 5:
    print ("Looks like you're eating at: " + myChoice5 + "!")

