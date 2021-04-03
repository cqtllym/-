# 第七步
# 将final文件夹中文件进行数据清洗,筛选出语句
# 因为三种文件格式不同，所以分开进行
import os
from zimu.zimu.tools.langconv import *


# 繁体转简体
def TraditionalToSimplified(content):
    line = Converter("zh-hans").convert(content)
    return line


# 再一次筛选中文
cn = u'([\u4e00-\u9fa5]+)'
pattern_cn = re.compile(cn)

from_path = "../result/final_file/"
to_path = "../result/data_cleaning/"
if not os.path.isdir(to_path):
    os.makedirs(to_path)


# -----------------------------------------------------分割线----------------------------------------------------------
# 对ass文件进行数据清洗
# 首先备份处理，然后在备份文件上进行操作
filename = "ass.txt"
with open(from_path + filename, "r+") as f:
    with open(to_path+filename, "a+") as g:
        for line in f.readlines():
            if line.find('Dialogue') == 0 and len(line) < 500:
                fields = line.split(',')
                sentence = fields[len(fields) - 1]
                tag_fields = sentence.split('}')
                if len(tag_fields) > 1:
                    sentence = tag_fields[len(tag_fields) - 1]
                match_cn = pattern_cn.findall(sentence)
                w_sentence = Converter("zh-hans").convert(sentence)
                if len(match_cn) > 0:
                    try:
                        g.write(w_sentence)
                    except:
                        print(line)


# -----------------------------------------------------分割线----------------------------------------------------------
# 对ssa文件进行数据清洗
# 首先备份处理，然后在备份文件上进行操作
filename = "ssa.txt"
with open(from_path + filename, "r+") as f:
    with open(to_path+filename, "a+") as g:
        for line in f.readlines():
            if line.find('Dialogue') == 0 and len(line) < 500:
                fields = line.split(',')
                sentence = fields[len(fields) - 1]
                tag_fields = sentence.split('}')
                if len(tag_fields) > 1:
                    sentence = tag_fields[len(tag_fields) - 1]
                match_cn = pattern_cn.findall(sentence)
                w_sentence = Converter("zh-hans").convert(sentence)
                if len(match_cn) > 0:
                    try:
                        g.write(w_sentence)
                    except:
                        print(line)

# -----------------------------------------------------分割线----------------------------------------------------------
# 对srt文件进行数据清洗
# 首先备份处理，然后在备份文件上进行操作
filename = "srt.txt"
with open(from_path + filename, "r+") as f:
    with open(to_path+filename, "a+") as g:
        for line in f.readlines():
            match_cn = pattern_cn.findall(line)
            w_sentence = Converter("zh-hans").convert(line)
            if len(match_cn) > 0:
                try:
                    g.write(w_sentence)
                except:
                    print(line)


