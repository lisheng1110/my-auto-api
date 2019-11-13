import pytest
import requests
d = {}#创建一个空字典，引用全局变量
def test_login():#登录接口
    json_data = {
        "pwd": "xuepl1222",
        "userName": "xuepl1222"
    }
    r = requests.post(url="http://api.yansl.com:8084/login", json=json_data)
    print(r.json()['data']['token'])
    print(r.text)
    d['token'] = r.json()['data']['token']#修改字典的值，如果字典为空则为新增


def test_post_file(login):#参数里面引用conftest文件内的方法名
    f = open("c:\\Users\\guoya\\Desktop\实名认证接口.xlsx", "rb")  # ("文件路径ps：如果文件分割符是\要换成\\"，"二进制格式打开可读，")
    files = {"file": f}
    headers = {"token":login}  # 如果不需要登录则无需headers
    r = requests.post(url="http://api.yansl.com:8084/product/uploaProdRepertory", headers=headers, files=files)
    print(r.text, r.status_code)
    r.close()




