import requests
from utils.logger import logger
import json as _json


class HttpClient:
    __headers = {
        "content-type": "application/json;charset=UTF-8"
    }

    def __init__(self):
        # Session方法是全局的，可以简化Session配置
        self.__session = requests.session()

    def get(self, path, **kwargs):
        return self.__request(path, "GET", **kwargs)

    def post(self, path, data=None, json=None, **kwargs):
        return self.__request(path, "POST", data, json, **kwargs)

    def request(self, method, url, data=None, json=None, **kwargs):
        headers = kwargs.get("headers")
        params = kwargs.get("params")
        if headers:
            self.__headers.update(headers)

        resp = None

        self.__request_log(url, method, data, json, params, self.__headers)

        if method == "GET":
            resp = self.__session.get(url, *kwargs)
        elif method == "POST":
            resp = self.__session.post(url, data, json, **kwargs)
        elif method == "PUT":
            resp = self.__session.put(url, data, json, **kwargs)
        elif method == "DELETE":
            resp = self.__session.delete(url, data, json, **kwargs)
        else:
            logger.error("接口请求方式有误，请检查接口请求方式, 目前支持: {}".format(['GET', 'POST', 'PUT', 'DELETE']))
        self.__response_log(resp)
        return resp

    def __request(self, url, method, data=None, json=None, **kwargs):
        headers = kwargs.get("headers")
        params = kwargs.get("params")
        if headers:
            self.__headers.update(headers)
        self.__request_log(url, method, data, json, params, self.__headers)
        resp = None
        if method == "GET":
            resp = requests.get(url, **kwargs)
        elif method == "POST":
            # resp = self.__session.post(url, data, json, **kwargs)
            resp = requests.post(url, data, json, **kwargs)
        self.__response_log(resp)
        return resp

    @staticmethod
    def __request_log(url, method, data=None, json=None, params=None, headers=None):
        logger.info("接口请求地址: {}".format(url))
        logger.info("接口请求方式: {}".format(method))
        print(headers)
        if headers:
            logger.info("接口请求Header:\n{}".format(_json.dumps(headers, indent=4, ensure_ascii=False)))
        if params:
            logger.info("接口请求params参数:\n{}".format(_json.dumps(params, indent=4, ensure_ascii=False)))
        if data:
            logger.info("接口请求data参数:\n{}".format(_json.dumps(data, indent=4, ensure_ascii=False)))
        if json:
            logger.info("接口请求json参数:\n{}".format(_json.dumps(json, indent=4, ensure_ascii=False)))

    @staticmethod
    def __response_log(resp):
        try:
            logger.info("返回信息:\n{}".format(resp.text, ensure_ascii=False))
        except Exception as e:
            logger.error("发生错误:{}".format(e))