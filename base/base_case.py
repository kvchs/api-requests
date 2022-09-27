from utils.read_yaml_data import yaml_data
from base.http_client import HttpClient


class BaseCase:
    def __init__(self):
        self.url_data = yaml_data.load_yaml("api.yml")
        self.http_client = HttpClient()

