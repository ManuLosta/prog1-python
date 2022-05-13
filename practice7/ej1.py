sample_list = ['Red', 'Green', 'Yellow', '', 'White', 'Black', 'Pink', 'Yellow', 'Green']

def indexOfByIndex(list, string, index):
    if len(list) == index:
        return -1
    elif list[index] == string:
        return index  
    return indexOfByIndex(list, string, index + 1)

def indexOf(list, string):
    return indexOfByIndex(list, string, 0)

def indexOfEmpty(list):
    return indexOfByIndex(list, '', 0)

def put(list, string):
    empty = indexOfEmpty(list)
    if empty != -1:
        list[empty] = string
        return empty
    else:
        return -1

def remove(list, string, index = 0):
    if index == len(list):
        return 0
    elif list[index] == string:
        del list[index]
        return 1 + remove(list, string, index)
    else:
        return remove(list, string, index + 1)


print(indexOfByIndex(sample_list, 'Green', 2))
print(indexOf(sample_list, 'hola'))
print(indexOfEmpty(sample_list))
print(put(sample_list, 'Hola'))
print(sample_list)
print(remove(sample_list, 'Green'))
print(sample_list)