#!python3

"""
Werewolf Python Edition [0010-V0.3.0 pre6]
By CODEZPC
"""
try:
    # import
    import math
    import os
    import random
    import sys
    import time
    import shutil
    import character as c
    import func

    # launch
    i = 0
    os.system("cls")
    inp = input("Command(empty=start):$C$ ")
    os.system("cls")
    err = 0
    if inp.upper() == "RMC":#Remove Cache
        shutil.rmtree(".\\__pycache__")
        exit()
    elif inp.upper() != "DQS":#Devlop Quick Start
        print("狼人杀 Pro 正在启动中......\nTip:常运行Update.py可以保证版本更新哦")
        while i <= 10000:
            print("\r", end=" ")
            if i == 10000:
                os.system("cls")
                print("\033[0;32m完成!\n2024新春快乐!\033[0m")
                break
            else:
                print(
                    "{}% \033[0;33m[".format(i / 100),
                    "=" * (i // 400),
                    "\033[0m",
                    end=" ",
                )
            sys.stdout.flush()
            i += func.mx(i)
            time.sleep(random.randint(0, 5) / 100)
        time.sleep(2)
    # get character numbers
    err = 1
    while err:
        os.system("cls")
        try:
            cn = int(input("输入游戏人数 \033[0;34m(6-16)\033[0m :"))
        except:
            func.Enterr()
            time.sleep(1)
            continue
        else:
            err = 0
        if cn < 6 or cn > 16:
            err = 1
            func.Enterr()
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
                func.Enterr()
                time.sleep(1)
            else:
                if "D" in inp and "E" in inp:
                    func.Enterr()
                    time.sleep(1)
                    continue
                for i in inp:
                    if i not in check:
                        func.Enterr()
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
                func.Enterr()
                time.sleep(1)
            else:
                for i in inp:
                    if i not in check:
                        func.Enterr()
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
    # -gamemode
    err = 1
    while err:
        os.system("cls")
        try:
            inp = int(input("选择\033[0;34m游戏模式\033[0m：1 明牌  2 暗牌 :"))
        except:
            func.Enterr()
            time.sleep(1)
        else:
            if inp == 1 or inp == 2:
                mode = inp
                err = 0
            else:
                func.Enterr()
                time.sleep(1)
    # -freetalk
    err = 1
    while err:
        os.system("cls")
        try:
            inp = int(input("选择是否开启\033[0;34m自由讨论\033[0m：1 开  2 关 :"))
        except:
            func.Enterr()
            time.sleep(1)
        else:
            if inp == 1 or inp == 2:
                frtalk = inp
                err = 0
            else:
                func.Enterr()
                time.sleep(1)
    # -police
    err = 1
    while err:
        os.system("cls")
        try:
            inp = int(input("选择是否\033[0;34m竞选警长\033[0m：1 是  2 否 :"))
        except:
            func.Enterr()
            time.sleep(1)
        else:
            if inp == 1 or inp == 2:
                police = inp
                err = 0
            else:
                func.Enterr()
                time.sleep(1)
    # 实验功能 - 事件(还未准备前置！)
    """
    if cn >= 10:
        err = 1
        while err:
            os.system("cls")
            try:
                inp = int(input("选择是否开启\033[0;34m事件模式\033[0m：1 开  2 关 :"))
            except:
                pr.Enterr()
                time.sleep(1)
            else:
                if inp == 1 or inp == 2:
                    event = inp
                    err = 0
                else:
                    pr.Enterr()
                    time.sleep(1)
    """
    # starting
    os.system("cls")
    print("\033[0;32m所有设置已完成，\n开始启动主进程...\033[0m")
    time.sleep(1)
    os.system("cls")
    print("游戏参数:")
    print("人数:\033[0;34m", cn, "\033[0m")
    print("含有以下职业:")
    print("\033[0;34m2\033[0m 狼人")
    for i in "BCDEFGHIJKLMNOPQ":
        if cl[i]:
            print("\033[0;34m1\033[0m", cj[i].show())
    if mode == 1:
        print("模式：\033[0;34m明牌\033[0m")
    else:
        print("模式：\033[0;34m暗牌\033[0m")
    if frtalk == 1:
        print("自由讨论：\033[0;34m开\033[0m")
    else:
        print("自由讨论：\033[0;34m关\033[0m")
    if police == 1:
        print("竞选警长：\033[0;34m开\033[0m")
    else:
        print("竞选警长：\033[0;34m关\033[0m")
    print("\033[0;33m警告：在游戏过程中，输入错误则代表跳过！\033[0m")
    """
    if event == 1:
        print("事件：\033[0;34m开\033[0m")
    else:
        print("事件：\033[0;34m关\033[0m")
    """
    os.system("pause")
    # main
    day = 0
    while True:
        day += 1
        os.system("cls")
        print("第" + str(day) + "夜")
        time.sleep(1)
        # -s_wolf
        if cl["E"]:
            if not cl["A"]:
                inp = input("其他所有狼人已经死了，请选择你要杀的角色:")

        # -----NOT COMPLETED----- #

        # END
        break
    os.system("cls")
    for i in range(cn):
        if cn >= 10 and i < 9:
            print(end=" ")
        print(str(i + 1) + "号玩家:", player[i])
    os.system("pause")
except:
    os.system("cls")
    print("\033[0;31mOops!\033[0m")
    print("\033[0;31m): 程序运行出错\033[0m")
    print("\033[0;31m可能是输入错误 ，但是未被系统识别；\033[0m")
    print("\033[0;31m也有可能是程序意外错误 。\033[0m")
    print("\033[0;31m请重启程序，或联系开发人员(zpcpy@outlook.com)\033[0m")
    os.system("pause")
    exit()
