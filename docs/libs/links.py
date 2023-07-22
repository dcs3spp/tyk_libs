import json
import ruamel.yaml

from pathlib import Path


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


def get_path_set_from_urlcheck(input: Path) -> set[Path]:
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
            except json.JSONDecodeError:
                raise RuntimeError(f"Failed parsing {input}:{row+1}\t{line}")
            else:
                paths = paths | _find_unique_values_for_key(content, Key)

    return paths


def get_set_of_key_values_in_yaml(input: Path, key: str) -> set[Path]:
    paths = set()

    with input.open() as file:
        yaml = ruamel.yaml.YAML(typ="safe", pure=True)
        content = yaml.load(file)

        paths = _find_unique_values_for_key(content, key)

    return paths
