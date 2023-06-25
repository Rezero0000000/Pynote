import json

with open('data.json') as file:
    data = json.load(file)
       
def getCategories ():
    categories = []
    for row in data:
        category = []
        for key, value in row.items():

            if (key == "notes"):
                category.append(len(value))
                continue
            category.append(value)

        categories.append(category)

    return categories
