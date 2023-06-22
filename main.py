import os

os.system('cls')
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
    maxData = sorted(table_width + data_width, reverse = True)[:3]

    #print(sorted(maxData, reverse=True)[:3])
    print(maxData)
    
    #Create Header 
    header = "+" + "+".join("-" + "-" * (width+2) for width in table_width) + "+"
    table = []

    table.append(header)
    table.append("|" + "|".join( " " + header.ljust(table_width[i]) + " " for i, header in enumerate(headers)) + "|")
    table.append(header)


    for row in data:
        table.append("|" + "|" .join(" " + str(item).ljust(table_width[i]) + " " for i, item in enumerate(row)) + "|")

    table.append(header)
    return "\n".join(table)
    

data = [
    ["1", "Programming", 254],
    ["2", "Cyber Security", 43],
    ["3", "English", 140],
]
header = ['No', 'Categories', 'Notes']

table = createTable(data, header)
print(table)
    

#print("\n  +-------------------------+----------+")
#print("  | No | Categories         | Note     |")
#print("  |----|--------------------|----------|")
#print("  | 1  | Cyber Security     | 256      |")
