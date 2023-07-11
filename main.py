from ui import *
from data import getMenues
from diary import main_diary
from note import main_note
from todo import main_todo

import os
os.system('cls')

header = ['No', 'Menu', 'Items']
data = getMenues()
table = createTable(data, header)

print("\n\n\n")
printLogo()
printTitle("Menu")
print(table)

action = input(str('\nChose Menu --> '))

if (action == '1'):
    os.system("cls")
    print("\n\n\n")
    printLogo()
    printTitle("Diary");
    main_diary()
elif (action == '2'):
    os.system("cls")
    print("\n\n\n")
    printLogo()
    printTitle("Note");
    main_note()
elif (action == '3'):
    os.system("cls")
    print("\n\n\n")
    printLogo()
    printTitle("Todo List");
    main_todo()
else:
    print("Wrong input man")
    
