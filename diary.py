import argparse
from data import getItems, createItem, findItem, deleteItem, updateItem, search
from ui import createTable, printLogo, printPagination
import datetime
import os

def main_diary ():
    data = getItems(1)
    header = ["No", "Title", "Date"]
    page = 1
    total_page = len(data)
    table = createTable(data, header, page)

    print(table)
    printPagination(total_page, page)
        
    user_input = input("\nInput Argument argumen: ")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--read', type=int, help='Read Diary')
    parser.add_argument('-c', '--create', type=int, help='Create Diary')
    parser.add_argument('-u', '--update', type=int, help='Update Diary <id>')
    parser.add_argument('-d', '--delete', type=int, help='Delete diary <id>')
    parser.add_argument('-s', '--search', type=str, help='Search Diary <keyword> note: Input must string type')
    parser.add_argument('-p', '--page', type=int, help='Choice page')
    
    try:
        args = parser.parse_args(user_input.split())
        if(args.read):
            item = findItem(args.read,1);
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
            createItem(newDiary, 1)

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
            updateItem (updateData,1)

        elif (args.delete):
            deleteItem(args.delete, 1)

        elif (args.search):
            data = search(args.search, 1)
            table = createTable(data, header)
            os.system("cls")
            print("\n\n\n")
            printLogo()
            print(table)

        elif (args.page):    
            os.system('cls')
            print("\n\n\n")
            printLogo()
            table = createTable(data, header, args.page)
            print(table)
            printPagination(total_page, args.page)

    except argparse.ArgumentError:
        print("Argumen is not valid")
 
