import argparse
from data import getItems, createItem, findItem, deleteItem, updateItem, search, setStatus, getItemStatus, getRawItems
from ui import printMenu, printLogo, printPagination, clearScreen
import datetime
import os

def main_todo ():
    data = getItems(3)
    header = ["Todo", "Status"]
    page = 1
    total_page = len(data)
    printMenu(data, header, page)

    printPagination(total_page, page)
    user_input = input("\nInput Argument: ")
    
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--isFalse', type=int, help='set status false')
    parser.add_argument('-t', '--isTrue', type=int, help='set status true')
    parser.add_argument('-c', '--create', type=int, help='create todo')
    parser.add_argument('-u', '--update', type=int, help='update todo')
    parser.add_argument('-d', '--delete', type=int, help='delete todo')
    parser.add_argument('-l', '--list', type=int, help='list todo <1 = true> <0 = false>')
    parser.add_argument('-p', '--page', type=int, help='Choice page')

    try:
        args = parser.parse_args(user_input.split())
        if (args.create):
            title = str(input("Title : "))
            now = datetime.datetime.now()
            date = now.strftime("%d-%B-%Y")

            newDiary = {
                "id": len(getRawItems(3)) + 1, 
                "title": title, 
                "status": False
            }
            createItem(newDiary, 3)
            print("Data sucessfully Created")

        if (args.list):
            data = getItemStatus(True)
            clearScreen() 
            printMenu(data, header, page, "true")

        elif(args.list == False):
            data = getItemStatus(False)
            clearScreen()
            printMenu(data, header, page, "false")

        elif (args.update):
            title = str(input("New title : "))
            now = datetime.datetime.now()
            date = now.strftime("%d-%B-%Y")

            updateData = {
                "id": args.update, 
                "title": title, 
                "status": False
            }
            updateItem (updateData,3)
            print("Data sucessfully Updated")

        elif (args.delete):
            deleteItem(args.delete, 3)
            print("Data sucessfully Deleted")

        elif (args.page): 
            clearScreen()
            if (args.page > len(data)):
                print("Data not found")
                printPagination(total_page, 1)
            else:
                printMenu(data, header, args.page)
                printPagination(total_page, args.page)

        elif (args.isTrue):
            setStatus(args.isTrue, True)

        elif (args.isFalse):
            setStatus(args.isFalse, False)

    except argparse.ArgumentError:
        print("Argument is not valid")
 
