import pytest
import allure
class Test_demo(object):
    @allure.feature("一级目录")
    def test_add(self):#测试等于
        assert 3+4==7
    def test_add2(self):#测试大于等于
        assert 30+1 >=32
    def test_in(self):
        a = "helloworld"
        b = "wo"
        assert b in a
if __name__ == '__main__':
    pytest.main(["-v","demo.py"])