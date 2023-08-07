import ruamel.yaml
import sys

from argparse import ArgumentParser
from pathlib import Path
from typing import IO, Any

from docs.libs.links import (
    PathTitlePair,
    get_path_set_from_urlcheck,
    get_set_of_key_values_in_yaml,
)


def find_missing_links_in_menu_yaml(urlcheck: Path, menu: Path) -> set[PathTitlePair]:
    """
    Find unique non alias paths that are in urlcheck file but not in menu.yaml

    @param urlcheck(Path) Path instance for urlcheck file
    @param menu(Path) Path instance for menu.yaml file

    @raise (RuntimeError) If json could not be decoded in urlcheck file
    """

    Key = "path"

    urlcheckSet = {i for i in get_path_set_from_urlcheck(urlcheck)}
    menuSet = {i for i in get_set_of_key_values_in_yaml(menu, Key)}

    diff = PathTitlePair.find_missing_paths(urlcheckSet, menuSet)

    return diff


def write_to_yaml(paths: set[PathTitlePair], out: IO[Any]) -> None:
    """
    Output to yaml file the set of paths

    @param paths(set[PathStringPair]) Set of file paths
    @param out(Path) Target yaml output file
    """

    items = []
    root = {"paths": items}

    for path in paths:
        item = {"path": f"{path.path}", "title": f"{path.title}"}
        items.append(item)

    yaml = ruamel.yaml.YAML()
    yaml.indent(sequence=4, offset=2)

    yaml.dump(root, out)


def run() -> int:
    """
    Run the check_menu_yaml_links CLI.

    Usage:
        python3 -m docs.cli.check_menu_yaml_links urlcheck=urlcheck.json menu=menu.yaml

    @return (int) Return exit status code
    """
    ErrorExitCode = 1
    SuccessExitCode = 0

    parser = ArgumentParser()
    parser.add_argument("--urlcheck", default="urlcheck.json")
    parser.add_argument("--menu", default="menu.yaml")

    args = parser.parse_args()

    urlcheckPath = Path(args.urlcheck)
    menuPath = Path(args.menu)

    if not urlcheckPath.exists():
        print(f"file {args.urlcheck} does not exist")
        return ErrorExitCode
    elif not menuPath.exists():
        print(f"file {args.menu} does not exist")
        return ErrorExitCode

    missingLinks = find_missing_links_in_menu_yaml(urlcheckPath, menuPath)

    count = len(missingLinks)

    if count > 0:
        print(
            "The urlcheck.json Hugo build file contains paths for all website content"
        )
        print("Some file paths have not been included in menu.yaml")
        print()
        print("Please remember to update menu.yaml with the path of new content files")
        print()
        print(f"{count} missing paths were found\n\n")

        write_to_yaml(missingLinks, sys.stdout)

        print(f"\nExit status code {ErrorExitCode}")
        return ErrorExitCode

    return SuccessExitCode
