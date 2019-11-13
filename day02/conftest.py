import pytest
import requests
#conftest.py解决 fixture函数不能跨模块的问题
#fixture函数定义函数内容执行的时机
#  scope的值 定义的是 fixture的作用范围，用到才会执行
#  session 在整个项目运行期间 ，只执行一次，无论有多少戈方法用到fixture函数
#  module  在整个模块运行期间 ，只执行一次，无论有多少戈方法用到fixture函数
#  class 在整个类运行期间 ，只执行一次，无论有多少戈方法用到fixture函数
# function  执行用到该 fixture函数的方法之前执行一次 ，
@pytest.fixture(scope='session')
def login():
    json_data = {
        "pwd": "xuepl1222",
        "userName": "xuepl1222"
    }
    r = requests.post(url="http://api.yansl.com:8084/login", json=json_data)
    token=(r.json()['data']['token'])
    print(token)
    return token


