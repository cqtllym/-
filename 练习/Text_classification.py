# 文本分类
import nltk

from nltk.corpus import movie_reviews
from nltk.corpus import brown
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())  # 统计词频，其中lower()函数将所有大写字母转化为小写字母
word_features = list(all_words.keys())[:2000]  # 取前2000个单词作为特征词数组
features = {}

def document_features(document):
    # 特征提取函数，每个特征都是形如contains(***)的key，value就是True或False，表示特征词数组中的这个词是否在文档中出现
    for word in word_features:
        features['contains(%s)' % word] = (word in document)
    return features


document = nltk.FreqDist(w.lower() for w in brown.words())

# document_word_txt = open("Text_classification/document.txt", "w")
# for document_word in document:
#     print(document_word, file=document_word_txt)
# document_word_txt.close()

# document_items_txt = open("Text_classification/document_items.txt", "w")
# for document_word,t in document.items():
#     print(document_word,t, file=document_items_txt)
# document_items_txt.close()


di = dict(document.items())  # 本身为list,因为列表中的元素为2，所以可以转为dict
print(type(document_features(document)))  # dict
featuresets = [document_features(document) for di in document]


classifier = nltk.NaiveBayesClassifier.train(featuresets)
classifier.classify(document_features(document))
classifier.show_most_informative_features(5)