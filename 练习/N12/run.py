from 练习.N12 import ltp

if __name__ == '__main__':
    text = "今天是开学的第4周。第9周我们将进行项目实训的中期答辩"
    text2 = "今天我感冒了，不能出去玩了"
    # # 中文分词(v1/cws)
    # ltp.main(text, "v1/cws")
    # # 词性标注(v1/pos)
    # ltp.main(text, "v1/pos")
    # # 依存句法分析(v1/dp)
    # ltp.main(text, "v1/dp")
    # # 命名实体识别(v1/ner)
    # ltp.main(text, "v1/ner")
    # # 语义角色标注(v1/srl)
    # ltp.main(text, "v1/srl")
    # 语义依存 (依存树) 分析(v1/sdp)
    ltp.main(text, "v1/sdp")
    # # 语义依存 (依存图) 分析(v1/sdgp)
    # ltp.main(text, "v1/sdgp")
    # # 关键词提取(v1/ke)
    # ltp.main(text, "v1/ke")
    # # 情感分析(v2/sa)
    # ltp.main(text2, "v2/sa")