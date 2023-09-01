def go():
    count = [0,0,0,0]
    n = int(input())
    for i in range(n):
        coord = input().split()
        if int(coord[0]) > 0 and int(coord[1]) > 0:
            count[0] += 1
        elif int(coord[0]) < 0 and int(coord[1]) > 0:
            count[1] += 1
        elif int(coord[0]) < 0 and int(coord[1]) < 0:
            count[2] += 1
        elif int(coord[0]) > 0 and int(coord[1]) < 0:
            count[3] += 1
    print('Первая четверть:',count[0])
    print('Вторая четверть:',count[1])
    print('Третья четверть:',count[2])
    print('Четвертая четверть:',count[3])

go()
