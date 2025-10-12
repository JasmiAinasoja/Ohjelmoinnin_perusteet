Children = 2
Hometown = "Nurmijärvi"
# Lista
TownsInFinland = ["Lahti", "Helsinki", "Nurmijärvi", "Lappeenranta", "Tampere"]

RandomInformation = ["Jasmi", 31, True, Children, Hometown]

print(TownsInFinland[0])
TownsInFinland.append("Rovaniemi")
print(TownsInFinland)
NumOfTowns = len(TownsInFinland)
print(TownsInFinland[NumOfTowns-1])

Municipalities = ["Asikkala", "Hollola", "Karvia", "Kempele"]
Towns = ["Lahti", "Helsinki", "Nurmijärvi", "Lappeenranta", "Tampere"]

MunicipalitiesAndTowns = [Municipalities, Towns]

print(MunicipalitiesAndTowns[1][-2])
Towns.sort()
print(Towns)

Teacher = {
    'name': 'Juha',
    'age': 50,
    'city': 'Lahti'
}

print(Teacher["name"])

Teacher['email'] = 'juha.hyytiäinen@lab.fi'

print(Teacher)

for key in Teacher:
    print(key, end=' ')
    print(Teacher[key])

Student = [
    {'name': 'Mikko', 'age': 25, 'city': 'Tampere'},
    {'name': 'Maija', 'age': 30, 'city': 'Espoo'},
    {'name': 'Seppo', 'age': 35, 'city': 'Helsinki'}
]
print(Student[0])

Cities = {
    'Finland': ['Tampere', 'Espoo', 'Helsinki'],
    'Sweden': ['Stockholm', 'Malmö']
}
print(Cities['Finland'][0])

for town in Towns:
    print(f"The town of {town}")
print(f"All the towns {Towns}")

for i in range(1,10):
    print(i)

for i in range(1,10):
    print(i, end=' ')

print("")
for i in range(1, 10, 3):
    print(i)

Total = 0
for i in range(1,101):
    Total +=i
    print(Total)

print(Total)

for i in range(9):
    if (i == 3):
        continue
    print(i)

# while 1 < 10:
#   print("Do not try me at home xD")

i = 0
while i < 10:
    print(f"Iteration number: {i}")
    i += 1
    # i = i + 1

continueLoop = True
while continueLoop == True:
    if input("Do you want to continue? ") != "yes":
        continueLoop = False

while True:
    if input("Do you want to continue? ") !="yes":
        break
    else:
        continue