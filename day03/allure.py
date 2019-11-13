import allure
import requests

'''
@allure.feature("模块1")#一级标签
@allure.story("接口1")#二级标签
@allure.title("用例描述1")#三级标签
def test_a():
    print("hello,world")

@allure.feature("模块1")
@allure.story("接口1")
@allure.title("用例描述2")
def test_a1():
    allure.attach("附件内容", "附件标题", allure.attachment_type.TEXT)

@allure.feature("模块1")
@allure.story("接口2")
@allure.title("用例描述")
def test_b():
    print("hello,world")

@allure.feature("模块2")
@allure.story("接口1")
@allure.title("用例描述")
def test_c():
    print("hello,world")

@allure.feature("模块2")
@allure.story("接口2")
@allure.title("用例描述")
def test_d():
    print("hello,world")'''


##############################################
# 添加操作步骤with allure.step,添加附件allure.attach("附件内容","附件标题",allure.attachment_Type.Text)
@allure.issue("http://www.baidu.com", "这是一个bug")
@allure.testcase("http://www.baidu.com", "哟用例")
@allure.feature("用户模块")
@allure.story("充值接口")
@allure.title("用例描述")
def test_change():
    with allure.step("准备请求数据"):
        json_data = {
            "accountName": "xuepl123",
            "changeMoney": 1
        }
    # 添加操作步骤with allure.step,添加附件allure.attach("","",allure.attachment_Type.Text)
    with allure.step("发送请求"):
        r = requests.post("http://api.yansl.com:8084/acc/recharge", json=json_data)

        allure.attach("""
        -------------请求-------------
        {}{}{}{}
        """.format(r.request.method, r.request.headers, r.request.url, r.request.body), "请求内容",
                      allure.attachment_type.TEXT)

    with allure.step("响应结果"):
        r = requests.post("http://api.yansl.com:8084/acc/recharge", json=json_data)
        allure.attach("""
        -------------响应-------------
        {}{}{}
        """.format(r.status_code, r.headers, r.text), "响应内容", allure.attachment_type.TEXT)
    with allure.step("判断结果"):
        allure.attach("""
        预期结果：{}
        --------------------------
        实际结果：{}
        """.format(200, r.status_code), "断言响应状态码", allure.attachment_type.TEXT)
        assert r.status_code == 200
        allure.attach("""
        预期结果：{}
        -------------------------------------
        实际结果：{}
        """.format(2000, r.text), "断言响应正文", allure.attachment_type.TEXT)
        assert "2000" in r.text
