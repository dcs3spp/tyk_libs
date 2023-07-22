from behave.runner import Context
from behave import given, use_fixture

from features.support.fixtures import setup_menu_mock, setup_urlcheck_mock


@given("a urlcheck file is mocked")
def step_impl_a_urlcheck_file_is_mocked(context: Context) -> None:
    use_fixture(setup_urlcheck_mock, context)


@given("a menu file is mocked")
def step_impl_a_menu_file_is_mocked(context: Context) -> None:
    use_fixture(setup_menu_mock, context)
