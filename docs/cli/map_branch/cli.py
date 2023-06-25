from argparse import ArgumentParser
from docs.libs.core import extract_semver


def map_from_branch(branch_name: str) -> str:
    """
    Map a branch name to tyk-docs branch naming scheme

    @param branch_name(str) The source branch name

    @returns (str) The mapped branch name
    """
    result = extract_semver(branch_name)

    return f"release-{result}"


def run() -> str:
    """
    Run the map_release_branch CLI.

    Usage:
        python3 -m docs.cli.map_branch.map_release_branch branch=release-5-lts
    """
    parser = ArgumentParser()
    parser.add_argument("branch")

    args = parser.parse_args()

    return map_from_branch(args.branch)
