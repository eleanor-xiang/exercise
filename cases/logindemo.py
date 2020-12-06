import pytest
import requests
import allure


@allure.feature("登录用例")
class Test_login(object):
    def test_setup(self):
        print("-------------------setup-----------------")
    def test_teardown(self):
        print("-------------------teardown-----------------")

    @pytest.mark.parametrize("username","password","act",["xiang","123456","act_login"])
    @allure.description("登录执行结果")
    @allure.title("第一个用例")
    def test_login(self,username,password,act):
        url = "http://localhost/upload/index.php"
        data = {
            "username":username,
            "password":password,
            "act":act
        }
        respond = requests.post(url,data=data)
        print(respond.json())
if __name__ == '__main__':
    pytest.main(["-v","logindemo.py"])