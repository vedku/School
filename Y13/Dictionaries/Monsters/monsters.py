import random

with open('monsters.txt', 'r') as file:
    content = file.readlines()

monsters_dict = {}
for line in content:
    name, description = line.strip().split(',', 1)
    monsters_dict[name] = description

def returning_description():
    monster_name = input("Which monster's description would you like to read?:")
    description = monsters_dict.get(monster_name)
    if description:
        print(f"{monster_name}: {description}")
    else:
        print(f"No information found for {monster_name}.")

dotheywantaname = int(input("Do you want some monster names to choose from? \n1 for yes\n0 for no\nInput here:"))

if dotheywantaname == 0:
    returning_description()
else:
    sample_names = random.sample(list(monsters_dict.keys()), min(5, len(monsters_dict)))
    for name in sample_names:
        print(name)
    returning_description()
