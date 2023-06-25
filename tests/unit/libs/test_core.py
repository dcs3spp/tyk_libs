import pytest

from hamcrest import assert_that, equal_to
from docs.libs.core import extract_semver


@pytest.mark.parametrize(
    "text,expected",
    [
        ("release-5-lts", "5"),
        ("release-5", "5"),
        ("release-4.2.3", "4.2"),
        ("release-4.2.0", "4.2"),
    ],
)
def test_extract_semver(text: str, expected: str) -> None:
    result = extract_semver(text)

    assert_that(result, equal_to(expected))


def test_extract_semver_raises_value_error_on_fail() -> None:
    text = "release"

    with pytest.raises(ValueError):
        _ = extract_semver(text)
