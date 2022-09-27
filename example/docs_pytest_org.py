import pytest


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5, "不相等"


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()


@pytest.mark.slow
def test_needsfiles(tmp_path):
    print(tmp_path)
    assert 0


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")


# class Fruit:
#     def __init__(self, name):
#         self.name = name
#         self.cubed = False
#
#     def cube(self):
#         self.cubed = True
#
#
# class FruitSalad:
#     def __init__(self, **fruit_bowl):
#         self.fruit = fruit_bowl
#         self._cube_fruit()
#
#     def _cube_fruit(self):
#         for fruit in self.fruit:
#             fruit.cube()
#
#
# @pytest.fixture()
# def fruit_bowl():
#     return [Fruit("apple"), Fruit("banana")]
#
#
# def test_fruit_salad(fruit_bowl):
#     # Act
#     fruit_salad = FruitSalad(*fruit_bowl)
#
#     # Assert
#     assert all(fruit.cubed for fruit in fruit_salad.fruit)
