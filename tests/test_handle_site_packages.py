from pathlib import (
    Path,
    PurePath,
    PureWindowsPath,
    PurePosixPath,
)
from typing import Union, cast

import pytest

from from_root.utils.get_project_root import _handle_site_packages


def _with_windows_copy(paths: tuple):
    return (
        paths,
        tuple(
            map(
                lambda path: (
                    path.replace('/', '\\')
                    if isinstance(path, str)
                    else path
                ),
                paths,
            )
        )
    )


@pytest.mark.parametrize(
    'path,expected_path',
    [
        *_with_windows_copy((
                '/python/site-packages/package',
                '/python/site-packages/package',
        )),
        *_with_windows_copy((
                '/python/site-packages/package/',
                '/python/site-packages/package/',
        )),
        *_with_windows_copy((
                '/python/site-packages/package/inner/whatever',
                '/python/site-packages/package',
        )),
        *_with_windows_copy((
                '/python/site-packages/package_x/inner_package/module.py',
                '/python/site-packages/package_x',
        )),
        *_with_windows_copy((
                '/python/error',
                None,
        )),
        *_with_windows_copy((
                '/python/site-packages/from_root',
                None,
        )),
    ]
)
def test_handle_site_packages(
        path: Union[str, PurePath],
        expected_path: Union[str, PurePath],
):
    path_type = (
        PureWindowsPath
        if '\\' in path
        else PurePosixPath
    )

    path = path_type(path)
    try:
        expected_path = path_type(expected_path)
    except TypeError:
        expected_path = None

    path = cast(Path, path)

    calculated_site_packages_path = _handle_site_packages(path)
    assert calculated_site_packages_path == expected_path
    assert type(calculated_site_packages_path) == type(expected_path)
