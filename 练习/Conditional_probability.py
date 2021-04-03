"""
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
"""
"""
以上是python2的写法，但是在python3中这个需要已经不存在了，这么做也不会什么实际意义。
在Python2.x中由于str和byte之间没有明显区别，经常要依赖于defaultencoding来做转换。
在python3中有了明确的str和byte类型区别，从一种类型转换成另一种类型要显式指定encoding。

但是仍然可以使用下面这个方法代替
"""

# 条件频率分布
import importlib,sys
importlib.reload(sys)

# 输出在布朗语料库中每个类别条件下每个词的概率
import nltk
from nltk.corpus import brown

# 链表推导式，genre是brown语料库里的所有类别列表，word是这个类别中的词汇列表
# (genre, word)就是类别加词汇对
genre_word = [(genre, word)
        for genre in brown.categories()
        for word in brown.words(categories=genre)
        ]
# 创建条件频率分布
cfd = nltk.ConditionalFreqDist(genre_word)

# 指定条件和样本作图
#cfd.tabulate()输出为表格.cfd.plot()输出为图像
cfd.plot(conditions=['news','adventure'], samples=[u'stock', u'sunbonnet', u'Elevated', u'narcotic', u'four', u'woods', u'railing', u'Until', u'aggression', u'marching', u'looking', u'eligible', u'electricity', u'$25-a-plate', u'consulate', u'Casey', u'all-county', u'Belgians', u'Western', u'1959-60', u'Duhagon', u'sinking', u'1,119', u'co-operation', u'Famed', u'regional', u'Charitable', u'appropriation', u'yellow', u'uncertain', u'Heights', u'bringing', u'prize', u'Loen', u'Publique', u'wooden', u'Loeb', u'963', u'specialties', u'Sands', u'succession', u'Paul', u'Phyfe'])

