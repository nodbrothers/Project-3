def go():
    s = [int(n) for n in input().split()]
    for i in range(0,len(s),2):
        if i == len(s)-1 and (len(s) % 2 != 0):
            continue
        else:
            s[i],s[i+1] = s[i+1],s[i]
    print(*s)

go()