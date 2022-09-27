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


class Foo:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val


def pytest_assertrepr_compare(op, left, right):
    """
    Defining your own explanation for failed assertions¶

    :param op:
    :param left:
    :param right:
    :return:
    """
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return [
            "Comparing Foo instances:",
            "   vals: {} != {}".format(left.val, right.val),
        ]


@pytest.mark.skip
def test_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2