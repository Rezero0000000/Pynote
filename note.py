import argparse
from data import getItems, createItem, findItem, deleteItem, updateItem, search
from ui import createTable, printLogo
import datetime
import os

def main_note ():
    data = getItems(2)
    header = ["No", "Title", "Date"]
    table = createTable(data, header)

    print(table) 
    user_input = input("\nInput argumen: ")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--read', type=int, help='Read Note')
    parser.add_argument('-c', '--create', type=int, help='Create Note')
    parser.add_argument('-u', '--update', type=int, help='Update Note <id>')
    parser.add_argument('-d', '--delete', type=int, help='Delete Note <id>')
    parser.add_argument('-s', '--search', type=str, help='Search Note <keyword> note: Input must string type')
    
    try:
        args = parser.parse_args(user_input.split())
        if(args.read):
            item = findItem(args.read,2);
            if (item):
                print("\n")
                print("Title:", item['title'])
                print("Date:", item['date'])
                print("\nMessage:\"", item['message'],'"')
            else:
                print("Data not found")

        elif (args.create):
            title = str(input("Title : "))
            message = str(input("Message : "))
            now = datetime.datetime.now()
            date = now.strftime("%d-%B-%Y")

            newDiary = {
                "id": len(data) + 1, 
                "title": title, 
                "message": message, 
                "date": date
            }
            createItem(newDiary, 2)

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
            updateItem (updateData,2)

        elif (args.delete):
            deleteItem(args.delete, 2)

        elif (args.search):
            data = search(args.search, 1)
            table = createTable(data, header)
            os.system("cls")
            print("\n\n\n")
            printLogo()
            print(table)

    except argparse.ArgumentError:
        print("Argumen is not valid.")
 
