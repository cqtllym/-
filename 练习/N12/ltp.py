# 自然语言处理，包含
# 以下为v1/
# 中文分词(cws)，
# 词性标注(pos)，
# 依存句法分析(dp)，
# 命名实体识别(ner)，
# 语义角色标注(srl)，
# 语义依存 (依存树) 分析(sdp),
# 语义依存 (依存图) 分析(sdgp)
# 关键词提取(ke)

# 情感分析(v2/sa)
import time
import urllib.request
import urllib.parse
import json
import hashlib
import base64

# text 为string 类型，不超出500字节
def main(text, kind):
    body = urllib.parse.urlencode({'text': text}).encode('utf-8')
    url = 'http://ltpapi.xfyun.cn/'+kind
    api_key = '2908c767b1b8826f5255fb21eda04526'
    param = {"type": "dependent"}

    x_appid = '0cacbead'
    x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode('utf-8'))
    x_time = int(int(round(time.time() * 1000)) / 1000)
    x_checksum = hashlib.md5(api_key.encode('utf-8') + str(x_time).encode('utf-8') + x_param).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    req = urllib.request.Request(url, body, x_header)
    result = urllib.request.urlopen(req)
    result = result.read()
    print(result.decode('utf-8'))
    return


if __name__ == '__main__':
    main()