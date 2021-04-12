# 第八步，内容过滤
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!未完成

import sys
import re
import os


if __name__ == '__main__':
    # illegal=ur"([\u2000-\u2010]+)"
    illegal = u"([\u0000-\u2010]+)"
    pattern_illegals = [re.compile(u"([\u2000-\u2010]+)"), re.compile(u"([\u0090-\u0099]+)")]


    filters = ["字幕", "时间轴:", "校对:", "翻译:", "后期:", "监制:"]
    filters.append("时间轴：")
    filters.append("校对：")
    filters.append("翻译：")
    filters.append("后期：")
    filters.append("监制：")
    filters.append("禁止用作任何商业盈利行为")
    filters.append("http")
    htmltagregex = re.compile(r'<[^>]+>', re.S)
    brace_regex = re.compile(r'\{.*\}', re.S)
    slash_regex = re.compile(r'\\\w', re.S)
    repeat_regex = re.compile(r'[-=]{10}', re.S)

    path = "../result/data_cleaning"
    final = "../result/final_txt"
    if not os.path.isdir(final):
        os.makedirs(final)
    datanames = os.listdir(path)
    for i in datanames:
        f = open(path+"/"+i, "r+")
        g = open(final+"/"+i, "a+")
        while True:
            line = f.readline()
            if line:
                line = line.strip()

                # 关键词过滤
                need_continue = False
                for filter in filters:
                    try:
                        line.index(filter)
                        sys.stderr.write("filter keyword of %s %s\n" % (filter, line))
                        need_continue = True
                        break
                    except:
                        pass
                if need_continue:
                    continue

                # 去掉剧集信息
                if re.match('.*第.*季.*', line):
                    sys.stderr.write("filter copora %s\n" % line)
                    continue
                if re.match('.*第.*集.*', line):
                    sys.stderr.write("filter copora %s\n" % line)
                    continue
                if re.match('.*第.*帧.*', line):
                    sys.stderr.write("filter copora %s\n" % line)
                    line = ""
                    continue

                # 去html标签
                line = htmltagregex.sub('', line)

                # 去花括号修饰
                line = brace_regex.sub('', line)

                # 去转义
                line = slash_regex.sub('', line)

                # 去重复（这个没有做好）
                new_line = repeat_regex.sub('', line)
                if len(new_line) != len(line):
                    continue

                # 去特殊字符
                line = line.replace('-', '').strip()

                g.write(line+"\n")
            else:
                break
        f.close()
        g.close()
        pass