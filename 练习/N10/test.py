import pynlpir


pynlpir.open()
s = '聊天机器人到底该怎么做呢？'

# segments = pynlpir.segment(s,pos_english=False)
# for segment in segments:
#     print(segment[0], '\t', segment[1])

# key_words = pynlpir.get_key_words(s, weighted=True)
# for key_word in key_words:
#     print(key_word[0], '\t', key_word[1])
#
s = '刻晴怎么只会斩尽牛杂呢'
pynlpir.nlpir.ImportUserDict(b"mydict")  # 添加用户词典
segments = pynlpir.segment(s, pos_names='all', pos_english=False)
# 这里的segment是切词的意思，返回的是tuple(token, pos)，其中token就是切出来的词，pos就是语言属性
# 调用segment方法指定的pos_names参数可以是'all', 'child', 'parent'
# 默认是parent表示获取该词性的最顶级词性，child表示获取该词性的最具体的信息，all表示获取该词性相关的所有词性信息，相当于从其顶级词性到该词性的一条路径
for segment in segments:
    print(segment[0], '\t', segment[1])
pynlpir.close()
