import allure
import pytest
from requests.auth import HTTPBasicAuth

from base.http_client import HttpClient
from common.login import auth
from utils.read_yaml_data import yaml_data

http_client = HttpClient()

# 读取数据
auth_data = yaml_data.load_yaml("login.yml")


@allure.feature("登陆")
@allure.step("账号密码登陆")
def test_03():

    response = auth.login(auth=HTTPBasicAuth(auth_data['login_data']['json']['username'],
                                             auth_data['login_data']['json']['password'])).json()
    print(response)
    assert response.get("authenticated") is True


def test_session_post():
    response = auth.session_login(data={'key': 'value'}).json()
    assert response.get("url") == "https://httpbin.org/post"


if __name__ == '__main__':
    pytest.main()