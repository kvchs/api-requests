from configparser import ConfigParser
import pytest
from utils.read_yaml_data import yaml_data


def pytest_addoption(parser):
    parser.addoption("--env", action="store", help="choose env:test,dev,prod")
    parser.addini("env", help="choose env:test,dev,prod")


@pytest.fixture(scope='session')
def env_vars(request):
    config = request.config
    cur_env = config.getoption('--env') or config.getini('env')
    inifile = config.inifile
    conf = ConfigParser()
    conf.read(inifile)
    variables = {}
    if conf.has_section('global'):
        variables.update(conf.items('global'))
    if conf.has_section('cur_env'):
        variables.update(conf.items(cur_env))
    return variables


def test_demo(env_vars):
    print(env_vars)


@pytest.fixture(scope='session')
def apis(request):
    url_data = yaml_data.load_yaml("api.yml")
    return url_data
