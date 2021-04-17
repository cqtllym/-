from gensim.models import word2vec
import os
import gensim
import logging


def model_train(train_file_name, save_model_file):  # model_file_name为训练语料的路径,save_model为保存模型名

    # 模型训练，生成词向量
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.Text8Corpus(train_file_name)  # 加载语料
    try:
        model = gensim.models.Word2Vec(sentences, window=5, vector_size=200)  # 训练CBOW算法模型; 默认window=5
        model.save(save_model_file)
        model.wv.save_word2vec_format(save_model_file + ".bin", binary=True)   # 以二进制类型保存模型以便重用
    except:
        pass


def main():
    from_path = "../single_operation/word_segment_result/all.txt"
    save_model_name = 'zimu.model'
    if not os.path.exists(save_model_name):  # 判断文件是否存在
        model_train(from_path, save_model_name)
    else:
        print('此训练模型已经存在，不用再次训练')

    # 加载已训练好的模型
    model_1 = word2vec.Word2Vec.load(save_model_name)

    # # 将获得的词汇及其对应的向量按字典的格式存放到word_vector_dict中
    # word_vector_dict = {}
    # # print(model_1.wv.index_to_word)  # 获得所有的词汇
    # for word in model_1.wv.index_to_key:
    #     # model_1.wv.get_vector(word)  # 获得词汇及其对应的向量
    #     word_vector_dict[word] = model_1.wv.get_vector(word)
    # output_vector_file = 'word_vector.txt'
    # with open(output_vector_file, 'w', encoding='utf-8') as f:
    #     f.write(str(word_vector_dict))

    # 计算两个词的相似度/相关程度
    word1 = "学习"
    word2 = "快乐"
    y1 = model_1.wv.similarity(word1, word2)
    print("为：", y1)
    print("-------------------------------\n")

    # 计算某个词的相关词列表

    y2 = model_1.wv.most_similar(word2, topn=10)  # 10个最相关的
    print("和", word2, "最相关的词有：\n")
    for item in y2:
        print(item[0], item[1])
    print("-------------------------------\n")


if __name__ == "__main__":
    main()