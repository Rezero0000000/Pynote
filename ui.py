def printLogo ():

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

def printTodo (data, headers):
    print("\n")
    print("Todo                     Status")
    print("--------------------------------")
    for row in data:
        todo_str = f"          {[row[0]]}. {row[1]:<20}{row[2]}"
        print(todo_str)

def printTitle (title):
    print("  ===------ [ Hello World ] ------===")


def createTable (data, headers):
    # get Table Width
    table_width = [max(len(str(item)) for item in column)for column in zip(*data)]
    data_width = [len(header) for header in headers]

    maxData = []
    for i in range(3):
        tes = [table_width[i], data_width[i]]
        maxData.append(sorted(tes, reverse = True)[:1][0])
    
    #Create Header 

    header = "  +" + "+".join("-" * (width+2) for width in maxData) + "+"
    table = []

    table.append(header)
    table.append("  |" + "|".join(
        " " + header.ljust(maxData[i]) + " " for i, header in enumerate(headers)
    ) + "|")

    table.append("  |" + "|".join( 
        "-" * (maxData[i] + 2) for i, header in enumerate(headers)
    ) + "|")

    # Append row item
    for row in data: 
        table.append("  |" + "|" .join(
            " " + str(value).ljust(maxData[key]) + " " for key,value in enumerate(row)
        ) + "|")

    table.append(header)
    return "\n".join(table)


