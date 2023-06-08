import json

f = open("aquario.json", encoding="utf8")
aquario = json.load(f)
animais = aquario["data"]

def move_fishes_to_aquarium_42(animal):
    if animal["type"] == "fish":
        animal["tank number"] = 42
    return animal

print(list(map(move_fishes_to_aquarium_42, animais)))



