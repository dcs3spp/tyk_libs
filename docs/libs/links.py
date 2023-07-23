import json
import ruamel.yaml

from pathlib import Path
from typing import Any, Union


class PathTitlePair:
    def __init__(self, path: Path, title: str) -> None:
        self._path = path
        self._title = title

    @property
    def path(self) -> Path:
        return self._path

    @path.setter
    def path(self, value: Path) -> None:
        self._path = value

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        self._title = value

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, PathTitlePair):
            return False
        return self.path == other.path and self.title == other.title

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(self.path)

    @staticmethod
    def find_missing_paths(
        urlcheck: set["PathTitlePair"], menu: set[Path]
    ) -> set["PathTitlePair"]:
        diff = {pair for pair in urlcheck if pair.path not in menu}

        return diff


def _find_unique_values_for_key(data: dict, key: str) -> set[Path]:
    unique_values = set()

    def get_values(item: dict | list):
        if isinstance(item, dict):
            value = item.get(key)
            if value:
                unique_values.add(Path(value))
            for value in item.values():
                get_values(value)
        elif isinstance(item, list):
            for value in item:
                get_values(value)

    get_values(data)

    return unique_values


def get_path_set_from_urlcheck(input: Path) -> set[PathTitlePair]:
    Key = "path"

    paths = set()

    with input.open() as file:
        for row, line in enumerate(file):
            try:
                line = line.strip()
                if len(line) == 0:
                    continue

                content = json.loads(line)

                alias = content.get("alias")
                if alias:
                    continue

                path = content.get(Key)
                title = content.get("title")

                pair = PathTitlePair(Path(path), title)
                paths.add(pair)

            except json.JSONDecodeError:
                raise RuntimeError(f"Failed parsing {input}:{row+1}\t{line}")

    return paths


def get_set_of_key_values_in_yaml(input: Path, key: str) -> set[Path]:
    paths = set()

    with input.open() as file:
        yaml = ruamel.yaml.YAML(typ="safe", pure=True)
        content = yaml.load(file)

        paths = _find_unique_values_for_key(content, key)

    return paths
