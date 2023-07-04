from data import getItems
from ui import createTable

def main_diary ():
    data, messages = getItems(1)
    header = ["No", "Title", "Date"]
    table = createTable(data, header)

    print(table) 
    options = "\n\n[1]. Create  [2]. Read\n[3]. Update  [4]. Delete\n[5]. Search  [6]. Exit\n"
    print(options)
    action = input(str('[Diary] Chose Menu -> '))
 
