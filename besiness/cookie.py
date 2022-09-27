import pytest

from base.base_case import BaseCase


class CookieService(BaseCase):

    def cookie_error(self):
        resp1 = self.http_client.get(self.url_data['set_cookie']).json()
        resp2 = self.http_client.get(self.url_data['get_cookie']).json()
        return resp1, resp2
