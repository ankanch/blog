#encoding:utf-8
import os
fpath = "_posts/"
for f in os.listdir(fpath):
    title = ""
    date = ""
    with open(fpath + f,encoding="utf-8",errors="ignore") as f:
            line = f.readline()
            btitle = True
            bdate = True
            while len(line)>0 or btitle or bdate:
                if line.find("title:") > -1 and btitle:
                    title = line.replace("title: ","").replace("\n","").replace("'","").replace(":","").replace(",","").replace("。","").replace("\"","").replace("*","").replace("@","")
                    btitle = False
                    continue
                elif line.find("date:") > -1 and bdate:
                    date = line.replace("date: ","").replace("\n","").replace("'","").replace(":","").replace(",","").replace("。","").replace("\"","").replace("*","").replace("@","").split("T")[0]
                    bdate = False
                    pass
                if (btitle == False) and (bdate == False):
                    break
                line = f.readline()
    print(f.name,type(f),title,type(title))
    os.rename( f.name, fpath + date  + "-"  + title + '.md')