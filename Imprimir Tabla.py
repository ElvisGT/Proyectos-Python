def printTabla(args):
    for i in range(0,len(args)):
        ancho = [i] * len(args)
          
        


def main():
    tableData = [['apples', 'oranges', 'cherries', 'banana'], 
             ['Alice', 'Bob', 'Carol', 'David'], 
             ['dogs', 'cats', 'moose', 'goose']]

    printTabla(tableData)


if __name__ == "__main__":
    main()