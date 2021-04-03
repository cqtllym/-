# 第三步，查看文件的格式(只看两级就够了)
import os
path = "../result/unpack_files"
datanames = os.listdir(path)
a = dict()
for i in datanames:
    init = os.listdir(path + "/" + i)
    for j in init:
        bool = os.path.isdir(path + "/" + i + "/" + j)
        if bool:
            init2 = os.listdir(path + "/" + i + "/" + j)
            for k in init2:
                dr = k[-4:]
                if not dr in a.keys():
                    a[dr] = 0
                a[dr] += 1
        else:
            dr = j[-4:]
            if not dr in a.keys():
                a[dr] = 0
            a[dr] += 1
print(a)
# # 到上一步输出结果为
# {'.txt': 134, '.srt': 645, '.jpg': 86, '.png': 21, '.ass': 509, '.ssa': 26, '.vtt': 3, '英文字幕': 1, '.url': 56,
# ' III': 1, '.nfo': 1}
# 此时取多的三个字幕文件,即ssa,ass,srt,其他文件删除,其中英文字幕和 III是文件夹，直接删掉就行
