from pathlib import Path
from typing import List

import pytest
from pytest_mock import MockerFixture

from from_root import from_root
from from_root.get_project_root import ANCHORS


def path_exists(existing_paths: List[Path]):
    def inner(self: Path, *args, **kwargs):
        if self in existing_paths:
            return True
        return False

    return inner


_SITE_PACKAGES = Path('/python/site-packages/')
_USER_PROJECT = Path('/PyCharmProjects/project')


@pytest.mark.parametrize(
    'tb,existing_paths,root_path',
    [
        # Shallow cases:
        # 1. Basic
        *(
                (
                        (
                                _USER_PROJECT / 'module.py',
                        ),
                        (
                                _USER_PROJECT / anchor_file,
                        ),
                        _USER_PROJECT,
                )
                for anchor_file in ANCHORS
        ),
        # 2. `from_root` is called from a third party lib
        # but anchors exist in both user and third party projects
        *(
                (
                        (
                                _USER_PROJECT / 'module.py',
                                _SITE_PACKAGES / 'module.py',
                        ),
                        (
                                _USER_PROJECT / anchor_file,
                                _SITE_PACKAGES / '.project-root',
                        ),
                        _SITE_PACKAGES,
                )
                for anchor_file in ANCHORS
        ),

        # Deep cases
        # 1. Basic
        *(
                (
                        (
                                _USER_PROJECT / 'inner_package1' / 'inner_package2' / 'module.py',
                        ),
                        (
                                _USER_PROJECT / anchor_file,
                        ),
                        _USER_PROJECT,
                )
                for anchor_file in ANCHORS
        ),
        # 2. `from_root` is called from a third party lib
        # but anchors exist in both user and third party projects
        *(
                (
                        (
                                _USER_PROJECT / 'inner_package1' / 'inner_package2' / 'module.py',
                                _SITE_PACKAGES / 'inner_package1' / 'inner_package2' / 'module.py',
                        ),
                        (
                                _USER_PROJECT / anchor_file,
                                _SITE_PACKAGES / '.project-root',
                        ),
                        _SITE_PACKAGES,
                )
                for anchor_file in ANCHORS
        ),
        # No anchors case
        (
                (
                        _USER_PROJECT / 'module.py',
                ),
                (),
                None,
        ),
    ],
)
def test_from_root(
        tb: List[Path],
        existing_paths: List[Path],
        root_path: Path,
        mocker: MockerFixture,
):
    tb = [
        mocker.Mock(filename=str(path))
        for path in tb
    ]
    mocker.patch(
        'traceback.extract_stack',
        return_value=tb,
    )
    mocker.patch.object(Path, 'exists', path_exists(existing_paths))

    if root_path is None:
        with pytest.raises(FileNotFoundError):
            from_root()
    else:
        calculated_root = from_root()
        assert Path(root_path) == calculated_root
