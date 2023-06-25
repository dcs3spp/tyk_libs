from behave.runner import Context
from behave import given, then, when
from hamcrest import assert_that, equal_to

from docs.cli.map_branch.cli import map_from_branch


@given("the source branch is named {branch_name}")
def step_impl_source_branch_named(context: Context, branch_name: str) -> None:
    context.branch_name = branch_name


@when("the map_branch command is run")
def step_impl_map_branch_command(context: Context) -> None:
    try:
        context.map_branch_cmd_result = map_from_branch(context.branch_name)
    except ValueError:
        context.error_raised = True


@then("the mapped branch name should be {expected_result}")
def step_impl_command_result(context: Context, expected_result: str) -> None:
    assert_that(context.map_branch_cmd_result, equal_to(expected_result))


@then("an error should be raised")
def step_impl_an_error_should_be_raised(context: Context) -> None:
    assert_that(context.error_raised, equal_to(True))
