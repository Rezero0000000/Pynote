import json
import math
import re

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

def paginate(data, items_per_page):
    total_items = len(data)
    total_pages = math.ceil(total_items / items_per_page)
    paginated_data = []

    for page in range(total_pages):
        start_index = page * items_per_page
        end_index = start_index + items_per_page
        page_data = data[start_index:end_index]
        paginated_data.append(page_data)

    return paginated_data

def getItems (id):
    rawItems = getRawItems(id)
    items1 = []

    for row in rawItems:
        item = []
        for key, value in row.items():
            if (key == "message"):
                continue
            item.append(value)
        items1.append(item)
    
    paginate_item = paginate(items1, 5)
    return paginate_item 
    
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

def updateItem (updateItem, menu_id):
    for menu in data:
        if (menu['id'] == menu_id):
            for item in menu['items']:
                if(item['id'] == updateItem['id']):
                    item['title'] = updateItem['title']
                    item['message'] = updateItem['message']
                    item['date'] = updateItem['date']
    
    with open('data.json', 'w') as file:
        json.dump(data, file)

def search (regex_pattern, menu_id):
    rawItems = getRawItems(menu_id)
    data = []

    for row in rawItems:
        item = []
        for key, value in row.items():
            if (key == "message"):
                continue
            item.append(value)
        data.append(item)
    
    search_result = []

    for item in data:
        if re.search(regex_pattern, item[1], re.IGNORECASE):
            search_result.append(item)
    
    finalResult = []
    if len(search_result) > 0:
        for item in search_result:
            finalResult.append(item)

    paginate_item = paginate(finalResult, 5)

    return paginate_item
  
 
def setStatus (item_id, status):
    for item in data[2]['items']:
        if (item['id'] == item_id):
            item['status'] = status

    with open('data.json', 'w') as file:
        json.dump(data, file)

def getItemStatus (status):
    items1 = []
    data = getRawItems(3)

    for d in data:
        if (int(d['status']) == status):
            item = []
            for key, value in d.items():
                if (key == "message"):
                    continue
                item.append(value)
            items1.append(item)

    items2 = []
    paginate_item = paginate(items1, 5)
    return paginate_item 
    
