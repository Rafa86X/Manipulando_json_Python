import json

f = open("aquario.json", encoding="utf8")
data_aquarium = json.load(f)
animals = data_aquarium["data"]

def verify_fish(animal):
    if animal["type"] == "fish":
        return True
    return False

def verify_shellfish(animal):
    if animal["type"] == "shellfish":
        return True
    return False

def verify_turtle(animal):
    if animal["type"] == "turtle":
        return True
    return False

animals_fish = list(filter(verify_fish, animals))
animals_shellfish = list(filter(verify_shellfish, animals))
animals_turtle = list(filter(verify_turtle, animals))

print('\n',animals_fish)
print('\n',animals_shellfish)
print('\n',animals_turtle)
