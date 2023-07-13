import argparse
from data import getItems, createItem, findItem, deleteItem, updateItem, search, setStatus, getItemStatus
from ui import printMenu, printLogo, printPagination
import datetime
import os

def main_todo ():
    data = getItems(3)
    header = ["Todo", "Status"]
    page = 1
    total_page = len(data)
    printMenu(data, header, page)

    printPagination(total_page, page)
    user_input = input("\nMasukkan argumen: ")
    
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--isFalse', type=int, help='lol')
    parser.add_argument('-t', '--isTrue', type=int, help='lol')
    parser.add_argument('-c', '--create', type=int, help='lol')
    parser.add_argument('-u', '--update', type=int, help='lol')
    parser.add_argument('-d', '--delete', type=int, help='lol')
    parser.add_argument('-l', '--list', type=int, help='lol')
    parser.add_argument('-p', '--page', type=bool, help='Choice page')

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
        if (args.list):
            data = getItemStatus(True)
            os.system("cls")
            print("\n\n\n")
            printLogo()
            printMenu(data, header, page, "true")

        elif(args.list == False):
            data = getItemStatus(False)

            os.system("cls")

            print("\n\n\n")
            printLogo()
            printMenu(data, header, page, "false")

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

        elif (args.page):    
            os.system('cls')
            print("\n\n\n")
            printLogo()
            printMenu(data, header, page)
            printPagination(total_page, args.page)

        elif (args.isTrue):
            setStatus(args.isTrue, True)

        elif (args.isFalse):
            setStatus(args.isFalse, False)

    except argparse.ArgumentError:
        print("Argumen tidak valid.")
 
