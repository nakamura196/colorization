import os

path = '/Users/satoru/Downloads/abc/331900'
opath = '/Users/satoru/Downloads/obc'
file = '/Users/satoru/Downloads/abc/331900.sh'
f = open(file, 'w')
for x in os.listdir(path):
    if x.find("DS_Store") == -1:
        f.write("th /Users/satoru/git/siggraph2016_colorization/colorize.lua "+path+"/"+x+" "+opath+"/"+x+"\r\n")


f.close()
