import json

def loadData (path):
    with open(path) as file:
        data = json.load(file)
        return data
       
# categories = [[], [], []]


def getData ():
    items = loadData('data.json')
    categories = []
        
        #for data in item['notes']:
getData()
