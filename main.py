#!python3
# import
import math
import os
import random
import sys
import time
import character as c
import pr

# launch
os.system("cls")
err = 0
print("狼人杀 Pro (Terminal) 正在启动中......")
for i in range(1, 101):
    print("\r", end=" ")
    if i == 100:
        print(
            "\033[0;32m{}% [".format(i),
            "=" * (i // 4),
            "\033[0m",
            end="\033[0;32m]\033[0m",
        )
    else:
        print("{}% \033[0;33m[".format(i), "=" * (i // 4), "\033[0m", end=" ")
    sys.stdout.flush()
    time.sleep(random.randint(1, 30) / 100)
time.sleep(1)
# get character numbers
err = 1
while err:
    try:
        os.system("cls")
        cn = int(input("输入游戏人数 \033[0;34m(6-16)\033[0m :"))
    except:
        pr.Enterr()
        time.sleep(1)
        continue
    else:
        err = 0
    if cn < 6 or cn > 16:
        err = 1
        pr.Enterr()
        time.sleep(1)
# get character jobs
cl = {
    "A": 2,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0,
    "G": 1,
    "H": 1,
    "I": 1,
    "J": 1,
    "K": 0,
    "L": 0,
    "M": 0,
    "N": 0,
    "O": 0,
    "P": 0,
    "Q": 0,
}
cj = {
    "A": c.wolf,
    "B": c.k_wolf,
    "C": c.wk_wolf,
    "D": c.h_wolf,
    "E": c.s_wolf,
    "F": c.b_wolf,
    "G": c.witch,
    "H": c.hunter,
    "I": c.prophet,
    "J": c.guard,
    "K": c.cupid,
    "L": c.d_hunter,
    "M": c.bomber,
    "N": c.knight,
    "O": c.bear,
    "P": c.wild_child,
    "Q": c.g_keeper,
}
# -wolf
wn = math.floor(cn / 3)
ecn = wn - 2
cl["A"] = ecn
if ecn:
    err = 1
    while err:
        os.system("cls")
        check = ["B", "C", "D", "E", "F"]
        print("请选择\033[0;34m", ecn, "\033[0m个特殊狼选项:")
        print("B 狼王  C 白狼王  D 隐狼  E 石像鬼  F 狼美人")
        inp = input()
        if len(inp) != ecn:
            pr.Enterr()
            time.sleep(1)
        else:
            for i in inp:
                if i not in check:
                    pr.Enterr()
                    time.sleep(1)
                    break
                else:
                    del check[check.index(i)]
            else:
                err = 0
                for i in inp:
                    cl[i] = 1
# -god
ecn = cn - wn - 4
if ecn and ecn < 7:
    err = 1
    while err:
        os.system("cls")
        check = ["K", "L", "M", "N", "O", "P", "Q"]
        print("以下是已有的神职，你还需要再选择\033[0;34m", ecn, "\033[0m个:")
        print("女巫 猎人 预言家 守卫")
        print("请选择:")
        print("K 丘比特  L 猎人  M 炸弹人  N 骑士\nO 驯熊师  P 熊孩子  Q 守墓人")
        inp = input()
        if len(inp) != ecn:
            pr.Enterr()
            time.sleep(1)
        else:
            for i in inp:
                if i not in check:
                    pr.Enterr()
                    time.sleep(1)
                    break
                else:
                    del check[check.index(i)]
            else:
                err = 0
                for i in inp:
                    cl[i] = 1
elif ecn == 7:
    for i in "KLMNOPQ":
        cl[i] = 1
# -give
os.system("cls")
check = []
print("分配职位......")
for i in "ABCDEFGHIJKMNOPQ":
    if cl[i] > 0:
        for j in range(cl[i]):
            check.append(i)
player = []
for i in range(len(check)):
    j = random.choice(check)
    player.append(j)
    del check[check.index(j)]
for i in range(1, 101):
    print("\r", end=" ")
    if i == 100:
        print(
            "\033[0;32m{}% [".format(i),
            "=" * (i // 4),
            "\033[0m",
            end="\033[0;32m]\033[0m",
        )
    else:
        print("{}% \033[0;33m[".format(i), "=" * (i // 4), "\033[0m", end=" ")
    sys.stdout.flush()
    time.sleep(random.randint(1, 8) / 100)
time.sleep(1)
for i in "AAABCDEFGHIJKLMNOPQ":
    if i in player:
        player[player.index(i)] = cj[i]

os.system("cls")
for i in player:
    print(i)

input('运行结束，按"Enter"退出')
