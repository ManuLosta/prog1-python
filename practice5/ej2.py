rect1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
rect2 = ['Red', 'Green', 'Yellow', 'White', 'Black', 'Pink']
list1 = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]

def removeElements(list):
    return list[1:4] + list[6:] 

def addElements(list):
    list_copy = list[:]
    list_copy.insert(0, "Pink")
    list_copy.append("Yellow")
    return list_copy

def isEmpty(list):
    return len(list) == 0

def checkLists(list1, list2):
    return list1[2] == list2[2]

def listOfLists(list):
    return [list[0][:2], list[1][1:4], list[2][-2:]] 

print(removeElements(rect1))
print(addElements(rect1))
print(isEmpty(rect1))
print(checkLists(rect1, rect2))
print(listOfLists(list1))