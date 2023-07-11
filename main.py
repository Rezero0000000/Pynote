from ui import *
from data import getMenues
from diary import main_diary
from note import main_note

import os
os.system('cls')

header = ['No', 'Menu', 'Items']
data = getMenues()
table = createTable(data, header)

printLogo()
print(table)

action = input(str('\nChose Menu --> '))

if (action == '1'):
    os.system("cls")
    printLogo()
    main_diary()
elif (action == '2'):
    os.system("cls")
    printLogo()
    main_note()
elif (action == '3'):
    os.system("cls")
    printLogo()
else:
    print("Wrong input man")
    
