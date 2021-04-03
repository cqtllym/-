#双联词学习
import importlib,sys
importlib.reload(sys)

import nltk

# 举例解释双联词
sent = "to be or not to be"
tokens = nltk.word_tokenize(sent)
bigrm = nltk.bigrams(tokens)
print(*map(' '.join, bigrm), sep=', ')

def generate_model(cfdist, word, num=10):
    for i in range(num):
        print(word),
        word = cfdist[word].max()

# 加载语料库
text = nltk.corpus.genesis.words('english-kjv.txt')

# 生成双连词
bigrams = nltk.bigrams(text)

# 生成条件频率分布
cfd = nltk.ConditionalFreqDist(bigrams)

# 以we开头，生成双联词概率分布图
fd = cfd["we"]
fd.plot(10)

# 以we开头，生成随机串
generate_model(cfd, 'we')