# 第四步
# 清除非字幕文件，和少量字幕种类文件，以及三级文件夹，空文件夹
# 将ass, ssa, srt文件分类存储
import os
import shutil  # 清除三级文件夹用到的内置库
from shutil import copy

path = "../result/unpack_files"
datanames = os.listdir(path)
m0 = 0
n0 = 0
m1 = 0
n1 = 0
m2 = 0
n2 = 0
for i in datanames:
    init = os.listdir(path+"/"+i)

    # 清除垃圾文件
    for j in init:
        # 判断是否为文件夹
        bool3 = os.path.isdir(path + "/" + i + "/" + j)
        if bool3:
            init2 = os.listdir(path + "/" + i + "/" + j)
            for k in init2:
                bool3_0 = k.endswith(".ssa")
                bool3_1 = k.endswith(".ass")
                bool3_2 = k.endswith(".srt")
                if bool3_0 or bool3_1 or bool3_2:
                    if bool3_0:
                        if ((m0 % 200) == 0):
                            print("200 的倍数，新建一个文件夹")
                            n0 += 1
                        from_path = os.path.join(path+"/"+i+"/"+j, k)
                        to_path = "../result/classify/ssa/file_ssa"+ str(n0)
                        if not os.path.isdir(to_path):
                            os.makedirs(to_path)
                        copy(from_path, to_path)
                        m0 += 1
                    elif bool3_1:
                        if ((m1 % 200) == 0):
                            print("200 的倍数，新建一个文件夹")
                            n1 += 1
                        from_path = os.path.join(path+"/"+i+"/"+j, k)
                        to_path = "../result/classify/ass/file_ass"+ str(n1)
                        if not os.path.isdir(to_path):
                            os.makedirs(to_path)
                        copy(from_path, to_path)
                        m1 += 1
                    elif bool3_2:
                        if ((m2 % 200) == 0):
                            print("200 的倍数，新建一个文件夹")
                            n2 += 1
                        from_path = os.path.join(path+"/"+i+"/"+j, k)
                        to_path = "../result/classify/srt/file_srt"+ str(n2)
                        if not os.path.isdir(to_path):
                            os.makedirs(to_path)
                        copy(from_path, to_path)
                        m2 += 1

                else:
                    try:
                        print("删除垃圾文件：" + i + "/" + j + "/" + k)
                        os.remove(path + "/" + i + "/" + j + "/" + k)
                    except:
                        print("垃圾文件夹：" + i + "/" + j + "/" + k+"未处理")
                        shutil.rmtree(path + "/" + i + "/" + j + "/" + k)
                        print("删除垃圾文件夹：" + i + "/" + j + "/" + k)
        else:
            bool0 = j.endswith(".ssa")
            bool1 = j.endswith(".ass")
            bool2 = j.endswith(".srt")
            if bool0 or bool1 or bool2:
                # pass
                if bool0:
                    if ((m0 % 200) == 0):
                        print("200 的倍数，新建一个文件夹")
                        n0 += 1
                    from_path = os.path.join(path + "/" + i, j)
                    to_path = "../result/classify/ssa/file_ssa" + str(n0)
                    if not os.path.isdir(to_path):
                        os.makedirs(to_path)
                    copy(from_path, to_path)
                    m0 += 1
                elif bool1:
                    if ((m1 % 200) == 0):
                        print("200 的倍数，新建一个文件夹")
                        n1 += 1
                    from_path = os.path.join(path + "/" + i, j)
                    to_path = "../result/classify/ass/file_ass" + str(n1)
                    if not os.path.isdir(to_path):
                        os.makedirs(to_path)
                    copy(from_path, to_path)
                    m1 += 1
                elif bool2:
                    if ((m2 % 200) == 0):
                        print("200 的倍数，新建一个文件夹")
                        n2 += 1
                    from_path = os.path.join(path + "/" + i, j)
                    to_path = "../result/classify/srt/file_srt" + str(n2)
                    if not os.path.isdir(to_path):
                        os.makedirs(to_path)
                    copy(from_path, to_path)
                    m2 += 1
            else:
                try:
                    print("删除垃圾文件：" + i + "/" + j)
                    os.remove(path + "/" + i + "/" + j)
                except:
                    print("垃圾文件夹：" + i + "/" + j + "未处理")
                    shutil.rmtree(path + "/" + i + "/" + j)
                    print("删除垃圾文件夹：" + i + "/" + j )

# 删除空文件夹
for root, dirs, files in os.walk(path):
        if 0 == len(files) and len(dirs) == 0:
            print("删除空文件夹"+root)
            os.rmdir(root)



