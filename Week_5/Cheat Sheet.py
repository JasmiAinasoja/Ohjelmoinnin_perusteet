# print() # funktiokutsu
# print("Hello") # "Hello" on funktion paranmetri
# len()

#while True:
#   print("I can do this forever")

def greet(name):
    print("Hello")
    
print("Here I am")
name = "Jasmi"
greet(name)

def greet(name):
    return f"Hello, {name}"

print(greet("Jasmi"))

def greeting_airport(person, age):
    print(f"How do you do {person}")
    if age >= 18:
        print("Welcome to your flight")
    else:
        print(f"You need to wait for {18-age} years to flight solo.")

greeting_airport("Jasmi", 5)

#Tee ohjelma, joka kysyy käyttäjältä kokonaislukua. Testaa funktiolla, onko se alkuluku (prime number) vai ei.
#Kysy uutta lukua, kunnes käyttäjä pyytää lopettamaan kysymyksen.