# coding: utf-8
import matplotlib

matplotlib.use("agg")

import matplotlib.pyplot as plt

import seaborn as sns

import pandas as pd

sns.set()

id = "21827"
x = 5835
y = 4670
r = 12

#テキストファイルの読み込み
with open("logs/ssl_access_log", "r") as f:  #　txt形式の読み込み
    data = f.read()                # ひとまとまりのデータとして読み込む

data = data.split("\n")            #　改行コードで1行ずつに分割
hist = dict()
for i in range(0, len(data)):
    line = data[i]
    if line.find("/repo/iiif-img/"+id+"/") != -1 and line.find("default.jpg") != -1:
        # print(line)
        area = line.split("/repo/iiif-img/"+id+"/")[1].split("/")[0]
        if area not in hist:
            hist[area] = 0
        hist[area] = hist[area] + 1
        # print(area)
# print(data)                        #　'あきのたの...　と100行分表示
# print(len(data))                   #　100
# print(hist)



map = dict()
for i in range(0,x):
    map[i] = dict()
    for j in range(0,y):
        map[i][j] = 0

count = 0
for key in hist:
    count = count + 1
    print(str(count)+"\t"+str(len(hist)))
    key_tmp = key
    if key_tmp == "full":
        key_tmp = "0,0,"+str(x)+","+str(y)
    area3 = key_tmp.split(",")
    a0 = int(area3[0])
    b0 = int(area3[1])
    da = int(area3[2])
    db = int(area3[3])
    # print(str(a0)+","+str(b0)+","+str(da)+","+str(db))
    for l in range(a0, a0+da):
        for m in range(b0, b0+db):
            map[l][m] = map[l][m] + hist[key]


dx = int(x /r)
dy = int(y /r)

map2 = dict()

for i in range(0,r):
    x0 = dx * i
    x1 = x0 + dx
    if x1 > x:
        x1 = x
    map2[i] = dict()
    for j in range(0,r):
        y0 = dy * j
        y1 = y0 + dy
        if y1 > y:
            y1 = y

        max = 0



        for l in range(x0, x1):
            for m in range(y0, y1):
                if max < map[l][m]:
                    max = map[l][m]

        map2[i][j] = max

        # print(str(i)+","+str(j)+"="+str(max))

d = []

for yy in range(0,r):
    dd = []
    for xx in range(0,r):
        dd.append(map2[xx][yy])
    d.append(dd)

print(d)

# d = map2

df = pd.DataFrame(data=d)

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(x/100, y/100))

#g = sns.heatmap(df, annot=True, fmt="d", linewidths=.5, ax=ax, cbar=False)
g = sns.heatmap(df, cbar=False, xticklabels=False, yticklabels=False)

f.savefig(id+".png",bbox_inches="tight", pad_inches=0)
