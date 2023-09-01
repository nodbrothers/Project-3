def imt(m, h):
    imt_value = m / (h**2)
    questions = ['Недостаточная масса',
                 'Оптимальная масса', 'Избыточная масса']
    if 18.5 <= imt_value <= 26:
        return questions[1]
    elif imt_value < 18.5:
        return questions[0]
    else:
        return questions[2]


m, h = float(input()), float(input())
print(imt(m, h))
