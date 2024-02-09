import requests
import os

url = "https://github.com/CODEZPC/Werewolf/Version-Update.json"
r = requests.get(url)
f = open("TEMP", "w")
f.write(r.content)
VU = eval(open("Version-Update.json", "r").read())
VN = eval(open("TEMP", "r").read())
if VN.ver < VU.ver:
    for i in VU.file:
        url = "https://github.com/CODEZPC/Werewolf/" + i
        r = requests.get(url)
        f = open(i, "w")
        f.write(r.content)
    print("完成! 从第",VU.ver,"次更新升级到了第",VN.ver,"次!")
else:
    print("无需更新")
os.system("pause")