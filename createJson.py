import os
import json

path = 'input.json'
opath = path+"_out.json"
file = 'repot.json'

original = "写真帖『東京帝國大學』明治33年(1900)年版（東京大学総合図書館所蔵）"
after = "写真帖『東京帝國大學』明治33年(1900)年版（東京大学総合図書館所蔵）を改変"

with open(path, 'r') as f:
    data = json.load(f)
with open(file, 'r') as f2:
    data2 = json.load(f2)

canvases = data["sequences"][0]["canvases"]
canvases2 = data2["sequences"][0]["canvases"]
for i in range(0, len(canvases)):
    canvas = canvases[i]
    resource_2 = canvases2[i]["images"][0]["resource"]
    resource = canvas["images"][0]["resource"]
    resource_old = canvas["images"][0]["resource"].copy()
    resource_old["label"] = original
    resource["@type"] = "oa:Choice"

    resource["default"] = resource_old
    resource["item"] = []
    resource["item"].append(resource_2)
    resource_2["label"] = after

with open(opath, 'w') as outfile:
    json.dump(data, outfile)
