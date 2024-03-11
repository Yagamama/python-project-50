from gendiff import generate_diff
from pathlib import Path
from ..fixtures import big_strings


def test_generate_diff():
    p = Path(__file__)
    cur_dir = p.absolute().parent.parent.parent
    file1 = cur_dir.joinpath('jsons/file1.json')
    file2 = cur_dir.joinpath('jsons/file2.json')

    assert generate_diff(file1, file2) == big_strings.files1_and_2()
    assert generate_diff(file1, file1) == big_strings.files1_and_1()
