# 第五步，编码与转码
import os
import chardet
path = "../result/classify"
count = 0
for root, dirs, files in os.walk(path):
    for file in files:
        file_path = root + "/" + file
        f = open(file_path, 'rb+')
        data = f.read()
        f.close()
        encoding = chardet.detect(data)["encoding"]
        if encoding not in ("UTF-8-SIG", "UTF-16LE", "utf-8", "ascii"):
            try:
                gb_content = data.decode("gb18030")
                gb_content.encode('utf-8')
                f = open(file_path, 'w')
                f.write(gb_content.encode('utf-8'))
                f.close()
                print("finish:", file_path)
            except:
                count += 1
print("except:", count)