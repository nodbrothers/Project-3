def money(str):
    rub = len(str) * 60 // 100
    kop = len(str) * 60 % 100
    return f'{rub} р. {kop} коп.'


str = input()
print(money(str))
