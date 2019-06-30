
# Checks if two strings are anagrams, i.e. contain all the same letters.
def anagram(str1, str2):
    seen = {}
    for c in str1:
        if c not in seen.keys():
            seen[c] = 1
        else:
            seen[c] += 1
    for c in str2:
        if c not in seen.keys():
            return False
        else:
            seen[c] -= 1
            if seen[c] < 0:
                return False
    return sum(seen.values()) == 0

if __name__ == '__main__':
    test1 = ['abcd', 'dcba']
    if anagram(test1[0], test1[1]) != True:
        print('error 1')
    test2 = ['', 'ajb']
    if anagram(test2[0], test1[1]) == True:
        print('error 2')

