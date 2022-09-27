import pytest
from base.http_client import HttpClient
from utils.logger import logger
from utils.read_yaml_data import yaml_data
import requests

http_client = HttpClient()

url_data = yaml_data.load_yaml("api.yml")


@pytest.mark.webtest
def test_cookie_error():
    resp1 = http_client.get(url_data['set_cookie']).json()
    print(resp1)
    resp2 = http_client.get(url_data['get_cookie']).json()
    logger.warning(resp2['cookies'])
    try:
        assert resp2['cookies']['sessioncookie'] == '123456789'
    except KeyError:
        logger.info("cookie状态不保存场景")


def test_cookie_success():
    resp1 = http_client.request("GET", url_data['set_cookie']).json()
    print(resp1)
    resp2 = http_client.request("GET", url_data['get_cookie']).json()
    logger.warning(resp2['cookies'])
    assert resp2['cookies']['sessioncookie'] == '123456789'


if __name__ == '__main__':
    pytest.main()