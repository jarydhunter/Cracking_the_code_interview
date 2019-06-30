#Since this is python and strings are nicer here, I'm going to make some changes
# to the question.
# The function will take a list and reverse the order of the list, I can't use
# the length function, gotta write my own and I need to copy items one at a time,
# no list comprehensions. This is going to be a very unpythonic solultion. No,
# using reversed either! 'null' is my stand in for null terminator from c.


def flip_c_str(str):
    i = 0
    while str[i] != 'null':
        i += 1
    new_list = ['null'] * (i + 1)
    for j in range(i):
        new_list[j] = str[(i - 1) - j]
    return new_list

if __name__ == '__main__':
    test1 = ['null']
    correct1 = ['null']
    if flip_c_str(test1) != correct1:
        raise Exception("failed test1...")

    test2 = ['to', 'be', 'fair', 'null']
    correct2 = ['fair', 'be', 'to', 'null']
    if flip_c_str(test2) != correct2:
        raise Exception("failed test2..")

    test3 = ['r','a','c','e','c','a','r','null']
    correct3 = ['r','a','c','e','c','a','r','null']
    if flip_c_str(test3) != correct3:
        raise Exception("failed test3.")

    print("Great Success, So Nice!")
