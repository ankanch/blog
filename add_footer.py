#encoding:utf-8
import os
import datetime
fpath = "_posts"
footer = """{% include post_footer.md %}"""
fd = ""
with open("_includes/post_footer.md","r",encoding="utf-8",errors="ignore") as f:
    fd = f.read ()
with open("_includes/post_footer.md","w",encoding="utf-8",errors="ignore") as f:
    f.truncate()
    fd = fd.replace("@KTIME@",str(datetime.datetime.now()))
    f.write(fd)
for f in os.listdir(fpath):
    with open(fpath + "/" + f,encoding="utf-8",errors="ignore") as f:
        fd = f.read()
        if fd.find(footer) > -1:
            pass
        else:
            fd += "\r\n\r\n" + footer
    with open( f.name,"w",encoding="utf-8",errors="ignore") as f:
        f.truncate()
        f.write(fd)
