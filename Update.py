import zipfile
import os
import time
import shutil


def up():
    j = 0
    os.system("cls")
    print("更新中...")
    for i in f["files"]:
        j += 1
        os.system("cls")
        print("更新中...[", j, "/", f["num"], "]")
        x = open(".\\tmp\\" + i, "r", encoding="utf-8")
        y = open(i, "w", encoding="utf-8")
        y.write(x.read())
        x.close()
        y.close()


print(
    '请前往 https://codezpc.lanzouo.com/iJxBf1o06jfg 密码:1234567890\n下载ZIP文件，并重命名为"UD.zip"，然后放到C盘根目录下'
)
os.system("pause")
try:
    f = zipfile.ZipFile("C:\\UD.zip")
    f.extractall(".\\tmp")
    f.close()
except:
    print("错误，请重试")
    time.sleep(2)
    exit()
f = open(".\\tmp\\Version-Update.json", "r")
f = eval(f.read())
g = open("Version-Update.json", "r")
g = eval(g.read())
if g["ver"] < f["ver"]:
    up()
elif g["ver"] == f["ver"]:
    print("不需要更新，是否需要重新安装?[Y/N]")
    k = input()
    if k == "Y":
        time.sleep(0.3)
        up()
else:
    print("乱改文件想干啥?")
    time.sleep(0.8)
    up()
shutil.rmtree(".\\tmp")
