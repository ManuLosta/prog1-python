sample_list = ['Red', 'Green', 'Yellow', '', 'White', 'Black', 'Pink', 'Yellow', 'Green']

def indexOf(list, string):
    for i in range(len(list)):
        if list[i] == string:
            return i
    return -1

def indexOfByIndex(list, string, start):
    for i in range(start, len(list)):
        if list[i] == string:
            return i
    return -1

def indexOfEmpty(list):
    for i in range(len(list)):
        if list[i] == "":
            return i
    return -1

def put(list, string):
    for i in range(len(list)):
        if list[i] == "":
            list[i] = string
            return i
    return -1


def delete(list, string):
    deletes, i = 0, 0
    while i < len(list):
        if list[i] == string:
            del list[i]
            deletes += 1
        else:
            i += 1
    return deletes

print(indexOf(sample_list, 'Yellow'))
print(indexOfByIndex(sample_list, 'Yellow', 1))
print(indexOfEmpty(sample_list))
print(put(sample_list, 'Hola'))
print(sample_list)
print(delete(sample_list, 'Green'))
print(sample_list)
