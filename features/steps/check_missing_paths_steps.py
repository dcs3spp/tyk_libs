import json

from behave.runner import Context
from behave import then, when
from hamcrest import assert_that, equal_to

from pathlib import Path

from docs.cli.check_menu_yaml_links.cli import find_missing_links_in_menu_yaml


@when("the check_missing_links command is run")
def step_impl_when_check_missing_links_command_is_run(context: Context) -> None:
    context.missing_links_result = find_missing_links_in_menu_yaml(
        context.urlcheck_mock, context.menu_mock
    )


@then("the following missing links should be reported")
def step_impl_then_the_following_missing_links_should_be_reported(
    context: Context,
) -> None:
    if context.text is None:
        raise RuntimeError("failed to access attribute context.text")

    data = json.loads(context.text)

    expected_list = data.get("expected", [])
    expected_paths = {Path(path_dict.get("path")) for path_dict in expected_list}

    result = {pathTitlePair.path for pathTitlePair in context.missing_links_result}

    assert_that(result, equal_to(expected_paths))
