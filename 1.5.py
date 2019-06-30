# replace all spaces with '%20'
def rpl_spaces(str, replacement):
    new_str = []
    for c in str:
        if c == ' ':
            new_str.append(replacement)
        else:
            new_str.append(c)
    return ''.join(new_str)

if __name__ == '__main__':
    test1 = ' '
    if rpl_spaces(test1, '%20') != '%20':
        print('error 1')
    test2 = 'a b '
    if rpl_spaces(test2, '%20') != 'a%20b%20':
        print('error 2')