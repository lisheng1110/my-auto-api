import requests#主要发送http请求
# 1.get方法-请求无参数
'''r = requests.get("http://qa.yansl.com:8080/prefrenceArea/listAll")
# get请求无参数方法2发送请求，requests.request("请求方法","uri","参数")
#取请求方法
method=r.request.method
print(method)
#取URL
url=r.request.url
print(url)
#取请求头
headers=r.request.headers
print(headers)
#取响应状态码
statu_code=r.status_code
print(statu_code)
#取请求正文
body=r.request.body
print(body)
#取响应正文
text=r.text#文本格式
print(text)
d = r.json()#取json格式
print(d)
content=r.content#取二进制格式
print(content)
'''
###2.get方法-键值对数据
'''r = requests.get(url="http://api.yansl.com:8084/acc/getAccInfo?accountName=lisheng123")
print(r.status_code,r.text,r.url)
d={"accountName":"xuepl1222"}
r = requests.get(url="http://api.yansl.com:8084/acc/getAccInfo?",params=d)#关键字传参
print(r.status_code,r.text,r.url)'''
### 3.get方法-uri数据
r = requests.get(url="http://api.yansl.com:8084/acc/getAllAccs/1/3")
print(r.status_code,r.text,r.url)
r = requests.get(url="http://api.yansl.com:8084/acc/getAllAccs/{}/{}".format(1,3))
print(r.status_code,r.text,r.url)
