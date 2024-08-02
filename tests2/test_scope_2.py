import pytest


@pytest.fixture(scope="module", autouse=True)
def setup_session():
    print("module 2")


@pytest.fixture(scope="class", autouse=True)
def setup_module():
    print("class")


@pytest.fixture(scope="function", autouse=True)
def setup_fn():
    print("function 2")


class TestClass:
    def test_m1(self):
        print("test_m1")
        assert True

    def test_m2(self):
        print("test_m2")
        assert True