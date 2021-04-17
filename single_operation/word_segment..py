# 分词

import jieba
from jieba import analyse
import os


def segment(input, output):
    input_file = open(input, "r+")
    output_file = open(output, "a+", encoding='utf-8')
    while True:
        line = input_file.readline()
        if line:
            line = line.strip()
            seg_list = jieba.cut(line)
            segments = ""
            for str in seg_list:
                segments = segments + " " + str
            output_file.write(segments)
        else:
            break
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    from_path = "../zimu/zimu/result/final_txt"
    to_path = "word_segment_result"
    if not os.path.isdir(to_path):
        os.makedirs(to_path)
    datanames = os.listdir(from_path)
    for i in datanames:
        f_path = from_path+"/"+i
        g_path = to_path+"/all.txt"
        # f = open(f_path, "r+", encoding='utf-8')
        # g = open(g_path, "a+", encoding='utf-8')
        # print("from_path:", f_path, "to_path:", g_path)
        # f.close()
        # g.close()

        segment(f_path, g_path);