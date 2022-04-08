# Finds max value in given array
def find_max(a):
    curr_max = a[0]
    for i in a:
        if i > curr_max:
            curr_max = i

    return curr_max

def max_of_two(x, y):
    return find_max([x, y])

def max_of_three(x, y, z):
    return find_max([x, y, z])

print(max_of_two(6, 8))
print(max_of_three(9, 5, 34))
