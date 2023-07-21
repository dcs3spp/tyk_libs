import json
import yaml

from pathlib import Path


def _find_unique_values_for_key(yaml_data: dict, key: str) -> set[str]:
    unique_values = set()

    def get_values(item: dict | list):
        if isinstance(item, dict):
            if key in item:
                unique_values.add(item[key])
            for value in item.values():
                get_values(value)
        elif isinstance(item, list):
            for value in item:
                get_values(value)

    get_values(yaml_data)

    return unique_values


def read_urls(filePath: Path, key: str) -> set[str]:
    paths = set()

    with filePath.open() as file:
        for line in file:
            content = json.loads(line)
            paths = paths | _find_unique_values_for_key(content, key)

    return paths


def find_key_in_yaml(filePath: Path, key: str) -> set[str]:
    paths = set()

    with filePath.open() as file:
        content = yaml.safe_load(file)
        paths = _find_unique_values_for_key(content, key)

    return paths
