import os

f = open('./list.txt','w')

name_list = list()
for (dirpath, dirname, filename) in os.walk('data/'):
    for files in filename:
        name_list.append(files)

name_list = sorted(name_list)
for files in name_list:
    f.write(files+os.linesep)
f.close()