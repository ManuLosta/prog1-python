sample_list = ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']

def printList(list):
    for i in range(len(list)):
        print(f"{i}. \t {list[i]}")

def printBackwards(string):
    result = ""
    for i in range(1, len(string) + 1):
        result += string[-i]
    print(result)

printList(sample_list)
printBackwards('corcho')
