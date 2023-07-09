from ui import *
from data import getMenues
from diary import main_diary
from dream import main_dream

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
    main_dream()
    
