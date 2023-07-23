import pytest

from docs.libs.links import PathTitlePair
from pathlib import Path


@pytest.fixture
def path_string_pair_data():
    data = [
        (Path("/home/test1"), "string1"),
        (Path("/home/test2"), "string2"),
    ]
    return data


@pytest.fixture
def path_set_data():
    data = [
        Path("/home/test1"),
        Path("/home/test2"),
    ]
    return data


@pytest.fixture
def path_string_pair_set(path_string_pair_data):
    return set(PathTitlePair(*data) for data in path_string_pair_data)


@pytest.fixture
def path_set(path_set_data):
    return set(path_set_data)


def test_path_string_pair_set(path_string_pair_set, path_string_pair_data):
    assert len(path_string_pair_set) == len(path_string_pair_data)
    for path, string in path_string_pair_data:
        assert any(pair.path == path for pair in path_string_pair_set)


def test_path_set(path_set, path_set_data):
    assert len(path_set) == len(path_set_data)
    for path in path_set_data:
        assert path in path_set
