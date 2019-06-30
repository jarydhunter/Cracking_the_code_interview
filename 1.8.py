# Check string "rotation"

def check_rotation(str1, str2):
    if len(str1) != len(str2):
        return False

    tmp = str2 + str2
    if str1 in tmp:
        return True
    return False

if __name__ == '__main__':
    test1 = ["waterbottle","erbottlewat"]
    print(check_rotation(test1[0], test1[1]))

    test2 = ["",""]
    print(check_rotation(test2[0], test2[1]))

    test3 = ["abc","caba"]
    print(check_rotation(test3[0], test3[1]))

    test4 = ["123", "321"]
    print(check_rotation(test4[0], test4[1]))