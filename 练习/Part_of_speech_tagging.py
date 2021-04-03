# 词形归一、词性判断、词性标注
import nltk

# Stemming词干提取：一般是吧不影响词性的时态的小尾巴砍掉
porter = nltk.PorterStemmer()
print(porter.stem('lying'))  # 还原为lie

# Lemmatization词形归一：把各种类型的词的变形（查表），都归为一个形式
wordnet_lemmatizer = nltk.WordNetLemmatizer()
print(wordnet_lemmatizer.lemmatize('went')) # 不标注词性，这里直接使用无法还原，因为n.为温特
print(wordnet_lemmatizer.lemmatize('went',pos='v'))  # 先通过词性标注为动词，还原为go

# 词性判断
text1 = nltk.word_tokenize("I loved you")
print(nltk.pos_tag(text1))  # 最下方为各种词性标注

# 词性标注
tagged_token = nltk.tag.str2tuple("love/VB")
print(tagged_token)

sent = "我/NN 是/IN 一个/AT 大学生/NN"
for t in sent.split():
    print(nltk.tag.str2tuple(t))


"""
# 自己写的，对于一段文本，所有词性归一
def lemmatize_all(sentence):
    text = nltk.word_tokenize(sentence)
    for word,tag in nltk.pos_tag(text):
        if(tag.startswith("VB")):
            yield wordnet_lemmatizer.lemmatize(word,pos='v')
        elif(tag.startswith("NN")):
            yield wordnet_lemmatizer.lemmatize(word,pos='n')
        elif(tag.startswith("JJ")):
            yield wordnet_lemmatizer.lemmatize(word,pos='a')
        elif(tag.startswith("RB")):
            yield wordnet_lemmatizer.lemmatize(word, pos='r')
        else:
            yield word

train_f = []
sentence = "I thought you were better than me."
# 因为放在语句中才能判断其词性，所以不能拆分判断
train_f.append(' '.join(lemmatize_all(sentence)))
print(train_f)


# 以chesterton-brown.txt为例，先进行词性归一,!!!其中未进行特殊符号，标点的过滤清除
ta2 = []
text2 = nltk.corpus.gutenberg.raw('chesterton-brown.txt')
ta2.append(' '.join(lemmatize_all(text2)))
# 生成二联词
tokens = nltk.word_tokenize(ta2[0])  # 因为返回的文章都在数组ta2[0]中,所以此处应输入ta[0]
bigrams = nltk.bigrams(tokens)
# 生成条件分布
cfd = nltk.ConditionalFreqDist(bigrams)
# 以we开头，生成双联词概率分布图
fd = cfd["I"]
fd.plot(10)
"""

# CC - 并列连词 and, or
# IN - 介词或者从属连词(after, as long as, as though)
#
# CD - 基数词 one, two, 
# DT - 限定词（the, some, my）
# PDT - 前置限定词（both, a lot of）
# EX - 存在词（there）
# FW - 外来词
#
# JJ - 形容词 several, nice
# JJR - 形容词比较级
# JJS - 形容词最高级
#
# LS - 列表标记
# MD - 情态动词
#
# NN - 名词，单数
# NNS -名词，复数
# NNP - 专有名词，单数
# NNPS - 专有名词，复数
#
# POS - 所有格结尾(-’s)
# PRP - 人称代词(they, you)
# PRP$ - 所有格代名词(your, his)
#
# RB - 副词
# RBR - 副词的比较级
# RBS - 副词的最高级
#
# RP - 小品词（与动词构成短语动词的副词或介词 look for, take off）
# SYM - 符号
# TO - to
# UH - 感叹词(yes)
#
# VB - 动词原形
# VBD - 动词过去式
# VBG - 动名词或现在分词
# VBN - 动词过去分词
# VBP - 动词，非第三人称单数现在式
# VBZ - 动词，第三人称单数现在式
#
# WDT - wh-限定词(which)
# WP - wh-代名词(what)
# WP$ - 所有格的wh-代名词(whose)
# WRB - wh-副词(where, why)


