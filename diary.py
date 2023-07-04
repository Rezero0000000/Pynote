from data import getItems
from ui import createTable

def main_diary ():
    data, messages = getItems(1)
    header = ["No", "Title", "Date"]
    table = createTable(data, header)

    print(table)
    action = input(str('\n[Diary] Chose Menu --> '))
