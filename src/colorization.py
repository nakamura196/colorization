import os

path = '/Users/satoru/Downloads/hiraga/112929'
opath = '/Users/satoru/Downloads/hiraga/out'
file = '/Users/satoru/Downloads/hiraga/112929.sh'
f = open(file, 'w')
for x in os.listdir(path):
    if x.find("DS_Store") == -1:
        f.write("th /Users/satoru/git/siggraph2016_colorization/colorize.lua "+path+"/"+x+" "+opath+"/"+x+"\r\n")


f.close()
