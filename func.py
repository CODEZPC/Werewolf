import random


def Enterr():
    print("\033[0;31m输入错误，请重试。\033[0m")


def mx(n):
    if n + 75 < 10000:
        return random.randint(0, 75)
    else:
        return random.randint(0, 10000 - n)
