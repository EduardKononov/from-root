from pathlib import Path
from typing import List

import pytest
from pytest_mock import MockerFixture

from from_root import from_root


def path_exists(existing_paths: List[str]):
    def inner(self: Path, *args, **kwargs):
        if self in map(Path, existing_paths):
            return True
        return False

    return inner


@pytest.mark.parametrize(
    'tb,existing_paths,root_path',
    [
        *(
                (
                        (
                                '/python/site-packages/package_x/inner_package/module.py',
                                '/PyCharmProjects/project/uses_package_x.py',
                        ),
                        (
                                f'/PyCharmProjects/project/{anchor_file}',
                        ),
                        '/PyCharmProjects/project',
                )
                for anchor_file in ('.git', '.project-root')
        ),
        # `from_root` is called from `site-packages/package_x`
        (
                (
                        '/python/site-packages/package_x/inner_package/module.py',
                        '/PyCharmProjects/project/uses_package_x.py',
                ),
                [],
                '/python/site-packages/package_x',
        ),
        *(
                (
                        (
                                '/python/site-packages/package_x/inner_package/module.py',
                                '/PyCharmProjects/project/uses_package_x.py',
                        ),
                        (
                                f'/PyCharmProjects/project/{anchor_file}',
                                f'/PyCharmProjects/site-packages/package_x/{anchor_file}',
                        ),
                        '/PyCharmProjects/project',
                )
                for anchor_file in ('.git', '.project-root')
        ),
        # `project` and `package_y` both use `from_root`
        *(
                (
                        (
                                '/python/site-packages/package_x/inner_package/module.py',
                                '/PyCharmProjects/project/uses_package_x.py',
                                # this one uses `from_root`
                                '/python/site-packages/package_y/used_by_project_module.py',
                        ),
                        (
                                f'/PyCharmProjects/project/{anchor_file}',
                        ),
                        '/python/site-packages/package_y',
                )
                for anchor_file in ('.git', '.project-root')
        )
    ],
)
def test_from_root(
        tb: List[str],
        existing_paths: List[str],
        root_path: str,
        mocker: MockerFixture,
):
    tb = [
        mocker.Mock(filename=path)
        for path in tb
    ]
    mocker.patch(
        'traceback.extract_stack',
        return_value=tb,
    )
    mocker.patch.object(Path, 'exists', path_exists(existing_paths))
    calculated_root = from_root()
    assert Path(root_path) == calculated_root
