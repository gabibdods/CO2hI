people = [
    {"name": "Harry", "house": "Gryffindor"}
    {"name": "Draco", "house": "Slytherin"}
    {"name": "Cho", "house": "Ravenclaw"}
]

people.sort(key=lambda person: person["name"])

print(people)