from besiness.cookie import CookieService
from utils.logger import logger


def test_cookie_unshare():
    cookie_service = CookieService()
    resp1, resp2 = cookie_service.cookie_error()
    try:
        assert resp2['cookies']['sessioncookie'] == '123456789'
    except KeyError:
        logger.info("cookie状态不保存场景")