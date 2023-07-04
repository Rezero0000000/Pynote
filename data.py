import json

with open('data.json') as file:
    data = json.load(file)
       
def getMenues ():
    menues = []
    for row in data:
        menu = []
        for key, value in row.items():

            if (key == "items"):
                menu.append(len(value))
                continue
            menu.append(value)

        menues.append(menu)

    return menues
