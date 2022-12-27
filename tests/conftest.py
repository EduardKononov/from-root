from pathlib import Path
from typing import List, Optional, Tuple

import pytest
from pytest_mock import MockerFixture


def path_exists(existing_paths: Tuple[Path, ...]):
    def inner(self: Path, *args, **kwargs):
        if self in existing_paths:
            return True
        return False

    return inner


@pytest.fixture
def mock_get_project_root(
        mocker: MockerFixture,
):
    def mock(
            tb: List[Path],
            existing_paths: Tuple[Path, ...] = (),
            disable_exists_mock: bool = False,
    ):
        tb = [
            mocker.Mock(filename=str(path))
            for path in tb
        ]
        mocker.patch(
            'traceback.extract_stack',
            return_value=tb,
        )
        if not disable_exists_mock:
            mocker.patch.object(Path, 'exists', path_exists(existing_paths))
        mocker.patch.object(Path, 'resolve', lambda self, *_: self)

    return mock
