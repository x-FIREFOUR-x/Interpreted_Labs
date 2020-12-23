def count(words):
    res = 0
    for i in range(len(words)):
        if palindrom(words[i]):
            res = res + 1
            print(words[i], end =' ')
    print()
    return res

def palindrom(word):
    flag = True
    for i in range(len(word)):
        if word[i] != word[len(word)-i-1]:
            flag = False
    return flag
