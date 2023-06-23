from data import getData
import os

os.system('cls')
#getData('data.json')

logoAscii = '''
     ___                   _        
    | _ \ _  _  _ _   ___ | |_  ___ 
    |  _/| || || ' \ / _ \|  _|/ -_)
    |_|   \_, ||_||_|\___/ \__|\___|
          |__/       
     -----------------------------
       -[ My Personal Library ]-
 '''
print(logoAscii)

def createTable (data, headers):
    # get Table Width
    table_width = [max(len(str(item)) for item in column)for column in zip(*data)]
    data_width = [len(header) for header in headers]

    maxData = []
    for i in range(3):
        tes = [table_width[i], data_width[i]]
        maxData.append(sorted(tes, reverse = True)[:1][0])

    #Create Header 

    header = "    +" + "+".join("-" * (width+2) for width in maxData) + "+"
    table = []

    table.append(header)
    table.append("    |" + "|".join( " " + header.ljust(maxData[i]) + " " for i, header in enumerate(headers)) + "|")
    table.append("    |" + "|".join( "-" * (maxData[i] + 2) for i, header in enumerate(headers)) + "|")
   
    # Append row item

    for row in data:
        for key,value in row:
            print(value)
        #table.append("    |" + "|" .join(" " + str(item).ljust(maxData[key]) + " " for key, value in row) + "|")

    table.append(header)
    return "\n".join(table)

header = ['No', 'Categories', 'Notes']
data = [
        {"index":"1", "name":"Programming", "notes":254},
        {"index":"1", "name":"Programming", "notes":254},
        {"index":"1", "name":"Programming", "notes":254},
   # ["2", "Cyber Security", 43],
   # ["3", "English", 140],
#    ["4", "Game", 140],
 #   ["5", "Just random thing", 140],
]

table = createTable(data, header)
print()
print(table)
print("    1, 2, 3 ->\n")
#action = input(str('Chose Your Action '))

