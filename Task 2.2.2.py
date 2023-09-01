def go():
    s = input().split()
    count = 0
    for i in range(len(s)-1):
        if int(s[i]) < int(s[i+1]):
            count += 1
    print(count)

go()
