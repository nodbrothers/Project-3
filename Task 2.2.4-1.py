def go():
    s = input().split()
    s1 = [s[-1]] + s[0:len(s)]
    print(*s1)

go()