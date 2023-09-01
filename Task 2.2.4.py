def evol():
    s = [int(num) for num in input().split()]
    s1 = []
    s1.append(s[-1])
    s1.extend(s[0:len(s)-1])
    print(*s1)

evol()