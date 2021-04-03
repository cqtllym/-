# 第一步
# 爬虫文件执行结束后，由于是使用split("?")进行文件判断命名，所以可能出现错误后缀，删除该文件即可
import os
path = "../result/download/files"
datanames = os.listdir(path)
for i in datanames:
    bool1 = i.endswith(".zip")
    bool2 = i.endswith(".rar")
    if bool1 or bool2:
        continue
    else:
        print(i)
        os.remove(path+"/"+i)