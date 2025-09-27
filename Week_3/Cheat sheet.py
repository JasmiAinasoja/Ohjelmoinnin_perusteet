print("Welcome to the temp app!")
Temp = int(input("What is the temperature of CPU? "))

if(Temp > 80):
    print("Warning, temperature too high!")
else:
    print("All cool, keep on going!")

# Tee ohjelma, joka testaa, onko annettu numero parillinen vai pariton.
num = int(input("Insert number: "))
Answer = num % 2
if Answer == 0:
    print(f"parillinen: {Answer}")
else:
    print(f"pariton: {Answer}")

if(Temp > 80):
    if(Temp > 90):
        print("You are toast")
else:
    print("Warning")

    if(Temp > 90):
        print("You are toast")
    elif(Temp > 80):
        print("Warning!")
    else:
        print("You are ok")

#Tee ohjelma, joka kysyy kahta nimeä. Testaa, kumpi nimistä on pidempi, vai onko ne saman mittaisia.
Name1 = input("Insert name1: ")
Name2 = input("Insert name2: ")
if(len(Name1) > len(Name2)):
    print(f"{Name1} on pidempi kuin {Name2}.")
elif len(Name2) > len(Name1):
    print(f"{Name2} on pidempi kuin {Name1}.")
else:
    print(f"{Name1} ja {Name2} ovat saman pituisia.")

Town = "Lahti"
Street = "Mukkulankatu"
Building = "19"

if(Town == "Lahti" and Street == "Mukkulankatu" and Building == 19):
    print("You are at LAB")
elif(Town == "Lahti" and (Street != "Mukkulankatu" or Building != 19)):
    print("You are in the correct town, but check the street address again")
elif not(Town == "Lahti" and Street == "Mukkulankatu" and Building == 19):
    print("You are completely lost...")

import random

print(random.random())
print(random.randint(1, 10))

# Tehtävä, tee yksinkertainen kivi, sakset, paperi peli random-metodia käyttäen.

