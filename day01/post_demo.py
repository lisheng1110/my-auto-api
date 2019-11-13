import requests

###post方法-无参数
# 参考get请求无参数模板

###post方法-键值对数据
'''data: 往请求正文中添加数据，
    如果数据格式为字符串类型，直接放到正文里边；
    若数据格式为字典类型，先转成键值对类型并放入请求正文中，并在请求头中添加Content-Type: application/x-www-form-urlencoded
headers: 往请求头中添加数据，数据类型为字典'''

# data = "accountName=xuepl1222"#方法一
# headers = {"Content-Type": "application/x-www-form-urlencoded"}
# r = requests.post(url="http://api.yansl.com:8084/acc/accLock", data=data, headers=headers)
# print(r.status_code, r.text, r.request.body)
# data={"accountName":"xuepl1222"}#方法二
# r = requests.post(url="http://api.yansl.com:8084/acc/accLock",data=data)
# print(r.status_code,r.text,r.request.body)


###post方法-json数据
json_data = '''{
  "accountName": "xuepl1222",
  "changeMoney": 10
}'''#方法一
# headers = {"Content-Type": "application/json"}
# r = requests.post(url="http://api.yansl.com:8084/acc/recharge", data=json_data, headers=headers)
# print(r.status_code, r.text, r.request.body)
#
# json_data={
#   "accountName": "xuepl1222",
#   "changeMoney": 1
# }#方法二
# r = requests.post(url="http://api.yansl.com:8084/acc/recharge", json =json_data)
# print(r.status_code, r.text, r.request.body)

# post方法-上传文件
f = open("c:\\Users\\guoya\\Desktop\实名认证接口.xlsx", "rb")#("文件路径ps：如果文件分割符是\要换成\\"，"二进制格式打开可读，")
files = {"file": f}
headers = {"token": "eyJ0aW1lT3V0IjoxNTczMDIyNjM2Mjc4LCJ1c2VySWQiOjE5NDMsInVzZXJOYW1lIjoic3RyMTIzIn0"}#如果不需要登录则无需headers
r = requests.post(url="http://api.yansl.com:8084/product/uploaProdRepertory", headers=headers,files=files)
print(r.text,r.status_code)
r.close()
