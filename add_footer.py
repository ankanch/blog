#encoding:utf-8
import os
import datetime
fpath = "_posts"
old_footer = ""
footer = """`© kanch` → [zl AT kanchz DOT com](kanchisme@gmail.com) → _posted at {{page.date}}_
_last updated on @KTIME@_""".replace("@KTIME@",str(datetime.datetime.now()))
for f in os.listdir(fpath):
    fd = ""
    with open(fpath + "/" + f,encoding="utf-8",errors="ignore") as f:
        fd = f.read()
        if fd.index(old_footer) > -1:
            fd = fd.replace(old_footer,footer)
        else:
            fd += "\r\n\r\n" + footer
    with open( f.name,"w",encoding="utf-8",errors="ignore") as f:
        f.truncate()
        f.write(fd)
