def commas(num):
    s = str(num)
    s1 = ''
    for i in range(1, len(s)+1):
        s1 = s[len(s) - i] + s1
        if i % 3 == 0 and num >= 1000 and i != len(s):
            s1 = ',' + s1

    return s1


n = int(input())
print(commas(n))
