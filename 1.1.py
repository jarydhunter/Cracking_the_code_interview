# Exercise 1.1 from the book Cracking the Coding Interview.
import string
import sys

def are_chars_unique(str):
    '''
    Check if all characters in the string str are unique.
    :param str: string
    :return: boolean
    '''

    seen = dict.fromkeys(string.printable, 0)
    for c in str:
        if seen[c] == 0 :
            seen[c] = 1
        else:
            return False
    return True

if __name__ == '__main__':
    if len(sys.argv) > 1:
        str = sys.argv[1]
    else:
        str = "I'm atesring" # should return true.
    print(are_chars_unique(str))
    sys.exit(are_chars_unique(str))