import ruamel.yaml

from argparse import ArgumentParser
from pathlib import Path

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


def write_to_yaml(paths: set[PathTitlePair], out: Path) -> None:
    """
    Output to yaml file the set of paths

    @param paths(set[PathStringPair]) Set of file paths
    @param out(Path) Target yaml output file
    """

    with out.open(mode="w") as file:
        items = []
        root = {"paths": items}

        for path in paths:
            item = {"path": f"{path.path}", "title": f"{path.title}"}
            items.append(item)

        yaml = ruamel.yaml.YAML()
        yaml.indent(sequence=4, offset=2)

        yaml.dump(root, file)


def run() -> None:
    """
    Run the check_menu_yaml_links CLI.

    Usage:
        python3 -m docs.cli.check_menu_yaml_links urlcheck=urlcheck.json menu=menu.yaml
    """
    parser = ArgumentParser()
    parser.add_argument("--urlcheck", default="urlcheck.json")
    parser.add_argument("--menu", default="menu.yaml")

    args = parser.parse_args()

    urlcheckPath = Path(args.urlcheck)
    menuPath = Path(args.menu)

    if not urlcheckPath.exists():
        print(f"file {args.urlcheck} does not exist")
        return
    elif not menuPath.exists():
        print(f"file {args.menu} does not exist")
        return

    missingLinks = find_missing_links_in_menu_yaml(urlcheckPath, menuPath)

    out = Path("missing_links.yaml")

    write_to_yaml(missingLinks, out)
