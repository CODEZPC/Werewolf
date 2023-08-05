#!python3
import character as c
import os
import sys
import time
import math
import random
os.system("cls")
err = 0
print("狼人杀 Pro (Terminal) 正在启动中......")
for i in range(1,101,random.randint(0,15)):
    if i > 100:
        i = 100
    print("\r",end=" ")
    print("{}% [".format(i),"="*(i//2),end=" ")
    sys.stdout.flush()
    time.sleep(random.randint(30,120)/100)
print("]")
time.sleep(1)
os.system("cls")
err = 1
while err:
    try:
        os.system("cls")
        cn = int(input("输入游戏人数 (6-16):"))
    except:
        print("输入错误，请重试。")
        time.sleep(1)
        continue
    else:
        err = 0
    if cn < 6 or cn > 16:
        err = 1
        print("输入错误，请重试。")
        time.sleep(1)
wn = math.floor(cn/3)
ewn = wn - 2
cl = {"A":2,"B":0,"C":0,"D":0,"E":0,"F":0,"G":1,"H":1,"I":1,"J":1,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0}
if ewn:
    err = 1
    while err:
        check = ["B","C","D","E","F"]
        os.system("cls")
        print("请选择",ewn,"个特殊狼选项:")
        print("B 狼王  C 白狼王  D 隐狼  E 石像鬼  F 狼美人")
        inp = input()
        if len(inp) != ewn:
            print("输入错误，请重试。")
            time.sleep(1)
        else:
            for i in inp:
                if i not in check:
                    print("输入错误，请重试。")
                    time.sleep(1)
                    break
                else:
                    del check[check.index(i)]
            else:
                err = 0