sample_list = ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']

def printList(list):
    for i in range(len(list)):
        print(f"{i}. \t {list[i]}")

def printBackwards(list):
    for i in range(-1, -len(list) - 1, -1):
        string = ""
        for j in range(-1, -len(list[i]) - 1, -1):
            string += list[i][j]
    
        print(f"{-i - 1}. \t {string}")


printList(sample_list)
print("\n")
printBackwards(sample_list)
