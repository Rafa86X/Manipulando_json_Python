import json

f = open("aquario.json", encoding="utf8")
data_aquarium = json.load(f)
animals = data_aquarium["data"]

def verify_fish(animal):
    if animal["type"] == "fish":
        return True
    return False

animals_fish = list(filter(verify_fish, animals))

def animal_name(animal):
    return animal["name"]


animals_fish_name = list(map(animal_name, animals_fish))
print(f'\n {animals_fish_name} \n')
