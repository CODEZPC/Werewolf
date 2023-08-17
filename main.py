#!python3
try:
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
    for i in "ABCDEFGHIJKLMNOPQ":
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
    for i in "AABCDEFGHIJKLMNOPQ":
        if i in player:
            player[player.index(i)] = cj[i]
    # config
    err = 1
    while err:
        os.system("cls")
        try:
            inp = int(input("选择游戏模式：1 明牌  2 暗牌 :"))
        except:
            pr.Enterr()
            time.sleep(1)
        else:
            if inp == 1 or inp == 2:
                mode = inp
                err = 0
            else:
                pr.Enterr()
                time.sleep(1)


    os.system("cls")
    for i in range(cn):
        print(str(i + 1) + "号玩家:", player[i])

    input('运行结束，按"Enter"退出')
except:
    os.system("cls")
    print("\033[0;31mOops!\033[0m")
    print("\033[0;31m): 程序运行出错\033[0m")
    print("\033[0;31m可能是 输入错误 ，但是未被系统识别；\033[0m")
    print("\033[0;31m也有可能是 程序意外错误 。\033[0m")
    print("\033[0;31m请重启程序，或联系开发人员(zpcpy@outlook.com)\033[0m")
    input('运行结束，按"Enter"退出')
