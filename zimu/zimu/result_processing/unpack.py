# 第二步
# 解压缩文件,删除未成功压缩的文件
import zipfile
from unrar import rarfile
import os
path = "../result/download/files"
datanames = os.listdir(path)
for i in datanames:
    bool1 = i.endswith(".zip")
    bool2 = i.endswith(".rar")
    if bool1:
        try:
            z = zipfile.ZipFile(path+"/"+i, 'r')
            filename = i[:-4]
            z.extractall(path="../result/unpack_files/"+filename+"/")
            z.close()
        except:
            print("未解压文件："+i)
            os.remove(path + "/" + i)
            print("未解压文件zip文件:"+i+"已删除")
    if bool2:
        try:
            unrars = rarfile.RarFile(path+"/"+i)
            filename = i[:-4]
            unrars.extractall(path="../result/unpack_files/"+filename+"/")
        except:
            print("未解压文件："+i)
            os.remove(path + "/" + i)
            print("未解压文件rar文件:"+i+"已删除")




