def num_reverse(num):
    if len(str(num)) == 5:
        return int(str(num)[::-1])
    else:
        return int(str(num)[:1] + str(num)[-1:-:-1])


print(num_reverse(int(input())))
