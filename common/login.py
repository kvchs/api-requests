from base.http_client import HttpClient


class Auth(HttpClient):

    def login(self, **kwargs):
        return self.get('https://httpbin.org/basic-auth/user/pass', **kwargs)

    def session_login(self, **kwargs):
        return self.request("POST", "https://httpbin.org/post", **kwargs)


auth = Auth()