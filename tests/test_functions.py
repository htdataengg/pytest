import pytest

from pyt.functions import f1

def setup_module(module):
    print(f"\nsetup_module: {module}")


def teardown_module(module):
    print(f"\nteardown_module: {module}")


def setup_function(fn):
    print(f"\nset up fn: {fn}")


def teardown_function(fn):
    print(f"\nteardown fn: {fn}")


def test_f1():
    assert f1() == "Hi"


def test_f2():
    assert f1() != "Hii"
