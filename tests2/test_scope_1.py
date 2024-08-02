import pytest


@pytest.fixture(scope="session", autouse=True)
def setup_session():
    print("\nsession")


@pytest.fixture(scope="module", autouse=True)
def setup_module():
    print("module 1")


@pytest.fixture(scope="function", autouse=True)
def setup_fn():
    print("function 1")


def test_1():
    print("test_1")
    assert True


def test_2():
    print("test_2")
    assert True
