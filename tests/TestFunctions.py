import pytest

from pyt.functions import f1


class TestFunctions:

    @classmethod
    def setup_class(cls):
        print(f"\nsetup_class: {cls}")

    @classmethod
    def teardown_class(cls):
        print(f"\nteardown_class: {cls}")

    def setup_method(self, fn):
        print(f"\nset up fn: {fn}")

    def teardown_method(self, fn):
        print(f"\nteardown fn: {fn}")

    def test_cf1(self):
        assert f1() == "Hi"

    def test_cf2(self):
        assert f1() != "Hii"
