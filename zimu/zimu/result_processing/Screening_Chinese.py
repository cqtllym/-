# 第六步，筛选中文
import chardet
import os
import re

cn = u'([\u4e00-\u9fa5]+)'
pattern_cn = re.compile(cn)
jp1 = u"([\u3040-\u309F]+)"
pattern_jp1 = re.compile(jp1)
jp2 = u"([\u30A0-\u30FF]+)"
pattern_jp2 = re.compile(jp2)
path = "../result/classify"
datanames = os.listdir(path)
to_path = "../result/final_file"
if not os.path.isdir(to_path):
    os.makedirs(to_path)
for i in datanames:
    init = os.listdir(path + "/" + i)
    for j in init:
        for root, dirs, files in os.walk(path+"/"+i+"/"+j):
            file_count = len(files)
            if file_count > 0:
                for index, file in enumerate(files):
                    f = open(root + "/" + file, "rb+")
                    content = f.read()
                    f.close()
                    encoding = chardet.detect(content)["encoding"]
                    try:
                        for sentence in content.decode(encoding).split('\n'):
                            if len(sentence) > 0:
                                match_cn = pattern_cn.findall(sentence)
                                match_jp1 = pattern_jp1.findall(sentence)
                                match_jp2 = pattern_jp2.findall(sentence)
                                sentence = sentence.strip()
                                if len(match_cn) > 0 and len(match_jp1) == 0 and len(match_jp2) == 0 and len(sentence) > 1 and len(sentence.split(' ')) < 10:
                                    if i == "ass":
                                        f = open("../result/final_file/ass.txt", 'a+')
                                        f.write(sentence)
                                        f.write("\n")
                                        f.close()
                                    elif i == "ssa":
                                        f = open("../result/final_file/ssa.txt", 'a+')
                                        f.write(sentence)
                                        f.write("\n")
                                        f.close()
                                    elif i == "srt":
                                        f = open("../result/final_file/srt.txt", 'a+')
                                        f.write(sentence)
                                        f.write("\n")
                                        f.close()
                    except:
                        continue