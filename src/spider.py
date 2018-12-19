import requests #导入requests库
from bs4 import BeautifulSoup

#r = requests.get('https://unsplash.com') #像目标url地址发送get请求，返回一个response对象
#print(r.text) #r.text是http response的网页HTML

#payload = {'key1': 'value1', 'key2': 'value2'}
#r = requests.post("http://httpbin.org/post", data=payload)
#r = requests.put("http://httpbin.org/put")
#r = requests.delete("http://httpbin.org/delete")
#r = requests.head("http://httpbin.org/get")
#r = requests.options("http://httpbin.org/get")

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'lxml')  #声明BeautifulSoup对象
find = soup.find('p')  #使用find方法查到第一个p标签
print("find's return type is ", type(find))  #输出返回值类型
print("find's content is", find)  #输出find获取的值
print("find's Tag Name is ", find.name)  #输出标签的名字
print("find's Attribute(class) is ", find['class'])  #输出标签的class属性值
print('NavigableString is：', find.string)

markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'lxml')
comment = soup.b.string
print(type(comment))
# <class 'bs4.element.Comment'>