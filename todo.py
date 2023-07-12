import argparse
from data import getItems, createItem, findItem, deleteItem, updateItem, search
from ui import printMenu, printLogo
import datetime
import os

def main_todo ():
    data = getItems(3)
    header = ["Todo", "Status"]

    printMenu(data, header)
    user_input = input("\nMasukkan argumen: ")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--create', type=int, help='lol')
    parser.add_argument('-u', '--update', type=int, help='lol')
    parser.add_argument('-d', '--delete', type=int, help='lol')
    parser.add_argument('-s', '--search', type=str, help='Lol')
    
    try:
        args = parser.parse_args(user_input.split())
        if (args.create):
            title = str(input("Title : "))
            message = title
            now = datetime.datetime.now()
            date = now.strftime("%d-%B-%Y")

            newDiary = {
                "id": len(data) + 1, 
                "title": title, 
                "message": message, 
                "date": date
            }
            createItem(newDiary, 3)

        elif (args.update):
            title = str(input("New title : "))
            message = str(input("New message : "))
            now = datetime.datetime.now()
            date = now.strftime("%d-%B-%Y")

            updateData = {
                "id": args.update, 
                "title": title, 
                "message": message, 
                "date": date
            }
            updateItem (updateData,3)

        elif (args.delete):
            deleteItem(args.delete, 3)

        elif (args.search):
            data = search(args.search, 1)
            os.system("cls")
            print("\n\n\n")
            printLogo()
            printMenu(data, header)

    except argparse.ArgumentError:
        print("Argumen tidak valid.")
 
