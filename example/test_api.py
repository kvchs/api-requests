import allure
import pytest
import requests
from requests.auth import HTTPBasicAuth

from base.http_client import HttpClient
from common.login import auth
from utils.read_yaml_data import yaml_data
from utils.read_json_data import json_data

http_client = HttpClient()

# 读取数据
auth_data = yaml_data.load_yaml("login.yml")
json_data = json_data.load_json("demo.json")


@allure.feature("测试API流程")
class TestApi:
    def test_01(self):
        response = requests.get('https://api.github.com/user', auth=('user', 'pass')).json()
        print(response)
        assert response.get("message") == "Requires authentication"

    @allure.story("测试allure story标签")
    def test_02(self):
        response = http_client.get('https://api.github.com/user', auth=('user', 'pass')).json()
        print(response)
        assert response.get("message") == "Requires authentication"

    @allure.step("步骤一")
    def test_03(self):
        print(auth_data['login_data'])
        # response = auth.login(auth=HTTPBasicAuth('user', 'pass')).json()
        response = auth.login(auth=HTTPBasicAuth(auth_data['login_data']['json']['username'],
                                                 auth_data['login_data']['json']['password'])).json()
        print(response)
        assert response.get("authenticated") is True

    @allure.step("步骤二")
    def test_04(self):
        print(json_data)


if __name__ == '__main__':
    pytest.main()
