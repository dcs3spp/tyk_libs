from behave import fixture
from behave.runner import Context

from features.support.mocks import setup_mock_file


@fixture
def setup_urlcheck_mock(context: Context):
    if context.text is None:
        raise RuntimeError(
            "setup_urlcheck_mock failed to access context.text attribute"
        )

    content = context.text.strip(" \n")

    yield from setup_mock_file(context, "urlcheck_mock", content, True)


@fixture
def setup_menu_mock(context: Context):
    if context.text is None:
        raise RuntimeError(
            "setup_urlcheck_mock failed to access context.text attribute"
        )

    yield from setup_mock_file(context, "menu_mock", context.text, False)
