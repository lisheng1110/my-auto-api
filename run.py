import pytest#pytest主要用于执行用例
#Terminnal输入框 输入pytest -s 执行所有test开头的用例
# pytest.main(['-k','关键字'])#pytest -k "关键字" 说明：执行用例包含“关键字”的用例
# pytest.main(['-m','标记'])#pytest -m ”标记“ 说明：执行特定的测试用例。
pytest.main(['-s','-v','day03/allure.py','--alluredir','report/xml'])

