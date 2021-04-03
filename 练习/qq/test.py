import re

data = []
# 读取数据集
file = open("C:/Users/asus/Desktop/tim消息导出/1.txt", encoding='utf-8')
last_name = ''
name = ''
multiLine = ''
flag = 0
count = 0
keyNoise = ['的口令红包', '邀请加入', '申请加入', '点击查看', '撤回了', '(无)', '对方已成功接收', '戳一戳', '自动回复']
for line in file:
    # 去除空行
    line = line.strip().replace('\n', '')
    if (len(line) == 0):
        continue
    # 去噪
    if (len(line) > 4 and (line[:4] == '消息记录' or line[:4] == '消息分组' or line[:4] == '消息对象' or line[:4] == '===='
                           or line[:4] == 'http' or line[:6] == '[QQ红包]' or line[:3] == '管理员')):
        continue
    continueflag = False
    for s in keyNoise:
        if (s in line):
            continueflag = True
    if (continueflag):
        continue
    if (line[:4] == '2020' or line[:4] == '2021'):
        continue

    # 去除图片和表情
    line = line.replace('[图片]', '')
    line = line.replace('[表情]', '')
    line = line.strip()
    # 去除空行
    if (len(line) == 3):
        continue
    if (len(line) == 0):
        continue
    data.append(line)
    count += 1
    if (count == 30678):  # 我这里只提取前30678行
        break
print(count)
# 写入数据
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(data))
