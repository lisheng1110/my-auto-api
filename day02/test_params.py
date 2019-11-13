
import pytest
import allure

a=[['猪','狗'],['不','如'],['禽','兽'],['不','如']]
@pytest.mark.parametrize("name",a)
def test_say_hi(name):
    print(name,"你好")


@allure.title("你好，世界")#一级标签
def test_a():
    print("hello,world")


