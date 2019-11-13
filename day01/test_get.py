import requests

def test_no_args():#get方法无参数
        r = requests.get("http://qa.yansl.com:8080/prefrenceArea/listAll")
        print(r.text)

def test_query():#get方法键值对参数
        r = requests.get(url="http://api.yansl.com:8084/acc/getAccInfo?accountName=lisheng123")
        print(r.status_code, r.text, r.url)

