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

def getRawItems (id):
    for item in data:
        if (item['id'] == id):
            return item['items']

def getItems (id):
    rawItems = getRawItems(id)
    items = []
    messages = []

    for row in rawItems:
        item = []
        message = []
        for key, value in row.items():
            if (key == "message"):
                message.append(value)
                continue
            item.append(value)
        messages.append(message)
        items.append(item)

    return items, messages
