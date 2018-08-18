import requests
import base64
from lxml import etree
import re

def request(url):
    html = requests.get(url)
    html.encoding = html.apparent_encoding
    return html.text

def parse_content(html):
    tree = etree.HTML(html)
    script_text = tree.xpath('//script/text()')[0]
    securty = re.findall(r'DSE8WyM[a-zA-Z0-9]+=*',script_text)
    return  securty

def base64_decode(String):
    byteStr = String.encode("utf8", "ignore")
    result = base64.b64decode(byteStr).decode("utf8", "ignore")
    return result

def decode(string):
    string = base64_decode(string)  #base64解码string参数,string参数的值就是上面代码中的那段base64编码后的内容
    key = "link@scmor.com..ok"        #Gword
    Len = len(key)               #Gword长度
    code = ''
    for i in range(0, len(string)):
        k = i % Len
        n = ord(string[i]) ^ ord(key[k])
        code += chr(n)
    return base64_decode(code)

request = request("http://ac.scmor.com/")
security_list = parse_content(request)
for security_text in security_list:
    print(decode(security_text))
