import pytest
from .fixtures import big_strings


@pytest.fixture(scope="module")
def files1_and_2():
    return big_strings.files1_and_2()


@pytest.fixture(scope="module")
def files1_and_1():
    return big_strings.files1_and_1()
