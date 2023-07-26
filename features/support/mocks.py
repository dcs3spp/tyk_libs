from contextlib import ExitStack
from pathlib import Path
from behave.runner import Context

from unittest.mock import MagicMock, patch


class FakeFile:
    def __init__(self, content, support_enumerate):
        self.content = content
        self.support_enumerate = support_enumerate
        self.position = 0

    def __iter__(self):
        if self.support_enumerate:
            return (line for _, line in enumerate(self.content.split("\n")))
        else:
            return iter(self.content.split("\n"))

    def read(self, size=None):
        if size is None:
            return self.content
        data = self.content[self.position : self.position + size]
        self.position += size
        return data

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass


def setup_mock_file(
    context: Context, attribute_name: str, content: str, support_enumerate: bool
):
    fake_file = FakeFile(content, support_enumerate)

    mock_path_instance = MagicMock(spec=Path)
    mock_path_instance.open.return_value.__enter__.return_value = fake_file

    setattr(context, f"{attribute_name}", mock_path_instance)

    with ExitStack() as stack:
        stack.enter_context(patch.object(Path, "open", return_value=mock_path_instance))
        yield
