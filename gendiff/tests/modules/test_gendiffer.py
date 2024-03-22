import pytest
from gendiff import generate_diff
from pathlib import Path
from ..fixtures import big_strings
from ...modules.plain import edit_plain_value
from ...modules.stylish import edit_value


@pytest.fixture
def filepath():
    p = Path(__file__)
    files_dir = p.absolute().parent.parent.parent
    return files_dir


def test_generate_diff(filepath):
    file1 = filepath.joinpath('test_files/file1.json')
    file2 = filepath.joinpath('test_files/file2.json')

    assert generate_diff(file1, file2, 'stylish') == big_strings.files1_and_2()
    assert generate_diff(file1, file1, 'stylish') == big_strings.files1_and_1()

    assert generate_diff(file1, file2, 'plain') == big_strings.f1_2_plain()
    assert generate_diff(file1, file1, 'plain') == ''


def test_generate_diff_yaml(filepath):
    file1 = filepath.joinpath('test_files/file3.yaml')
    file2 = filepath.joinpath('test_files/file4.yml')

    assert generate_diff(file1, file2, 'stylish') == big_strings.yml3_4()
    assert generate_diff(file2, file2, 'stylish') == big_strings.yml4_4()

    assert generate_diff(file1, file2, 'plain') == big_strings.yml3_4_plain()
    assert generate_diff(file1, file1, 'plain') == ''


def test_trees(filepath):
    file1 = filepath.joinpath('test_files/f1.json')
    file2 = filepath.joinpath('test_files/f2.json')
    file3 = filepath.joinpath('test_files/f1.yml')
    file4 = filepath.joinpath('test_files/f2.yml')

    assert generate_diff(file1, file2, 'stylish') == big_strings.tree_stylish()
    assert generate_diff(file1, file2, 'plain') == big_strings.tree_plain()
    assert generate_diff(file3, file4, 'stylish') == big_strings.tree_stylish()
    assert generate_diff(file1, file4, 'plain') == big_strings.tree_plain()


def test_edit_value():
    assert edit_value(55) == 55
    assert edit_value(False) == 'false'
    assert edit_value('str') == 'str'
    assert edit_value(None) == 'null'
    assert edit_value([77]) == 77
    res = '{\n      a: 1\n      b: {\n          c: 3\n      }\n  }'
    assert edit_value({'a': 1, 'b': {'c': 3}}) == res


def test_edit_plain_value():
    assert edit_plain_value(55) == 55
    assert edit_plain_value(False) == 'false'
    assert edit_plain_value('str') == "'str'"
    assert edit_plain_value(None) == 'null'
    assert edit_plain_value([77]) == 77
    assert edit_plain_value({'a': 1, 'b': {'c': 3}}) == '[complex value]'
