
# Doesn't really minimize buffer size
def rmv_dup(str):
    seen = set()
    out = []
    for char in str:
        if not (char in seen):
            seen.add(char)
            out.append(char)
    result = "".join(out)
    return result

if __name__ == '__main__':
    test1 = ""
    if rmv_dup(test1) != test1:
        print("you f'd up 1")

    test2 = 'aa'
    if rmv_dup(test2) != "a":
        print("you f'd up 2")

    test3 = 'aba'
    if rmv_dup(test3) != "ab":
        print("you f'd up 3")





