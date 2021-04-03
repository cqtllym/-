# 分词
# 英文分词：Tokenize,中文分词jieba.cut等
import nltk
import jieba
import jieba.posseg as posseg

sentence = "hello, world"
tokens = nltk.word_tokenize(sentence)
print(tokens)

# 中文分词:jieba
# 可以下载paddle模式，提高新词辨认率，但是会极大的增加辨认时间（本身已经很好了，使用paddle只会对新词进行优化辨认，其他的都差不多）

seg_list = jieba.cut("我来到山东山东大学", cut_all=True)
print("全模式:", "/ ".join(seg_list))  # 全模式
seg_list = jieba.cut("我来到山东山东大学", cut_all=False)
print("精确模式:", "/ ".join(seg_list))  # 精确模式
seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))
seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
# 搜索引擎模式
print(", ".join(seg_list))

seg_list = jieba.cut("可莉有蹦蹦炸弹，刻晴会斩尽牛杂")
print("添加自定义前：", ", ".join(seg_list))
# 添加自定义词典，添加的词典中每一行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒
seg_list = jieba.cut("可莉有蹦蹦炸弹，刻晴会斩尽牛杂")
jieba.load_userdict("自定义词典.txt")
print("添加自定义后：", ", ".join(seg_list))

# jieba进行分词及标注
# jieba.cut,生成的是一个生成器，generator，也就是可以通过for循环来取里面的每一个词
seg_list = jieba.cut("可莉有蹦蹦炸弹，刻晴会斩尽牛杂")
print(type(seg_list))
for word in seg_list:
    print(word)

# jieba.lcut 直接生成的就是一个list,也可以通过list(jieba.cut()) 来等价jieba.lcut()
seg_list = jieba.lcut("可莉有蹦蹦炸弹，刻晴会斩尽牛杂")
print(type(seg_list))
print(seg_list)

# posseg.cut 和 posseg.lcut的区别雷同，只不过posseg还提供了词性，方便对句法做分析
seg_list = posseg.cut("可莉有蹦蹦炸弹，刻晴会斩尽牛杂")
print(type(seg_list))
for word, flag in seg_list:
    print(word, flag)

seg_list = posseg.lcut("可莉有蹦蹦炸弹，刻晴会斩尽牛杂")
print(seg_list)