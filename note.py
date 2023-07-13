import argparse
from data import getItems, createItem, findItem, deleteItem, updateItem, search, getRawItems
from ui import createTable, printLogo, printPagination, clearScreen
import datetime
import os

def main_note ():
    data = getItems(2)
    header = ["No", "Title", "Date"]
    page = 1
    total_page = len(data)
    table = createTable(data, header, page)

    print(table) 
    printPagination(total_page, page)
    user_input = input("\nInput argumen: ")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--read', type=int, help='Read Note')
    parser.add_argument('-c', '--create', type=int, help='Create Note')
    parser.add_argument('-u', '--update', type=int, help='Update Note <id>')
    parser.add_argument('-d', '--delete', type=int, help='Delete Note <id>')
    parser.add_argument('-s', '--search', type=str, help='Search Note <keyword> note: Input must string type')
    parser.add_argument('-p', '--page', type=int, help='Choice page')
    
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
                "id": len(getRawItems(2)) + 1, 
                "title": title, 
                "message": message, 
                "date": date
            }
            createItem(newDiary, 2)
            clearScreen()
            print("Data sucessfully Created")

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
            clearScreen()
            print("Data sucessfully Updated")

        elif (args.delete):
            deleteItem(args.delete, 2)
            clearScreen()
            print("Data sucessfully Deleted")

        elif (args.search):
            data = search(args.search, 1)
            table = createTable(data, header, page)
            clearScreen() 
            print(table)
        
        elif (args.page):   
            clearScreen()
            if (args.page > len(data)):
                print("Data not found")
                printPagination(total_page, 1)
            else:
                table = createTable(data, header, args.page)
                print(table)
                printPagination(total_page, args.page)

    except argparse.ArgumentError:
        print("Argumen is not valid.")
 
