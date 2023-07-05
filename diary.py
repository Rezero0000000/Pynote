import argparse
from data import getItems, createDiary
from ui import createTable
import datetime

def main_diary ():
    data, messages = getItems(1)
    header = ["No", "Title", "Date"]
    table = createTable(data, header)

    print(table) 
    print("Type -h or --help for see list of command")
    user_input = input("\nMasukkan argumen: ")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--read', type=int, help='Pesan yang akan ditampilkan')
    parser.add_argument('-c', '--create', type=int, help='Pesan yang akan ditampilkan')
    parser.add_argument('-u', '--update', type=int, help='Pesan yang akan ditampilkan')
    parser.add_argument('-d', '--delete', type=int, help='Pesan yang akan ditampilkan')
    parser.add_argument('-s', '--search', type=str, help='Pesan yang akan ditampilkan')
    
    try:
        args = parser.parse_args(user_input.split())
        if(args.read):
            print(args.read)

        elif (args.create):
            title = str(input("Title : "))
            message = str(input("Message : "))
            now = datetime.datetime.now()
            date = now.strftime("%d-%B-%Y")

            newDiary = [{"id": len(data) + 1, "title": title, "message": message, "date": date}]
            createDiary(newDiary)

        elif (args.update):
            pass

        elif (args.delete):
            pass

        elif (args.search):
            pass
    except argparse.ArgumentError:
        print("Argumen tidak valid.")
 
