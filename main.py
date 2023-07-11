from ui import *
from data import getMenues
from diary import main_diary
from note import main_note
from todo import main_todo

import os
os.system('cls')

header = ['Menu', 'Items']
data = getMenues()

print("\n\n\n")
printLogo()
printMenu(data, header)

action = input(str('\nChose Menu --> '))

if (action == '1'):
    os.system("cls")
    print("\n\n\n")
    printLogo()
    main_diary()
elif (action == '2'):
    os.system("cls")
    print("\n\n\n")
    printLogo()
    main_note()
elif (action == '3'):
    os.system("cls")
    print("\n\n\n")
    printLogo()
    main_todo()
else:
    print("Wrong input man")
    
