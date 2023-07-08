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

    for row in rawItems:
        item = []
        for key, value in row.items():
            if (key == "message"):
                continue
            item.append(value)
        items.append(item)

    return items

def createItem (newData, id):
    for menu in data:
        if (menu['id'] == id):
            menu['items'].append(newData)

    with open('data.json', 'w') as file:
        json.dump(data, file)

def findItem (data_id, menu_id):
    items = getRawItems(menu_id);
    for item in items:
        if (item['id'] == data_id):
            return item

    return False

def deleteItem (data_id, menu_id):
        
    # Delete data
    for menu in data:
        if (menu['id'] == menu_id):
            for i,item in enumerate(menu['items']):
                if(item['id'] == data_id):
                     del menu['items'][i]
    
    # Reorder item
    for menu in data:
        if (menu['id'] == menu_id):
            for i, item in enumerate(menu['items']):
                item['id'] = i+1 
    
    with open('data.json', 'w') as file:
        json.dump(data, file)


