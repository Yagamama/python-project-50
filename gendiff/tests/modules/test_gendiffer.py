import pytest
from gendiff import generate_diff
from pathlib import Path
from ..fixtures import big_strings


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
