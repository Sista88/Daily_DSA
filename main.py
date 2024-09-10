def funct(s, k):
    max_vowels = 0
    st = ""
    count = 0
    cnt = 0
    lst = []
    len(s)
    i = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(0, len(s)):
        print("i is", i)
        if s[i] in vowels:
            count = count + 1
            print("letter is", "'", s[i], "'")
            print("count is", count)
        cnt = cnt + 1
        if cnt == 3:
            lst.append(count)
            cnt = 0
            count = 0
            print("list at", "'", i, s[i], "'", "is", lst)
    max_vowels = max(lst)
    return max_vowels


# print(funct("abciiidef", k=3))
print(funct("leetcode", k=3))
