def zodiak(year):
    zod = ["Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух",
           "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц"]
    if year > 2011:
        while year > 2011:
            year -= 12
        return zod[year % 2000]
    else:
        while year < 2012:
            if year + 12 > 2011:
                break
            year += 12
        return zod[year % 2000]


y = int(input())
print(zodiak(y))
