def amount(a, b):
    return a+b


def difference(a, b):
    return a-b


def compose(a, b):
    return a*b


def division(a, b):
    return a/b


def fun1(a, b):
    return a // b


def fun2(a, b):
    return a % b


def fun3(a, b):
    return (a**10 + b**10)**0.5


a, b = int(input()), int(input())

print(amount(a, b))
print(difference(a, b))
print(compose(a, b))
print(division(a, b))
print(fun1(a, b))
print(fun2(a, b))
print(fun3(a, b))
