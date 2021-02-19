from pathlib import Path
from typing import Iterable, Union

from from_root.get_project_dir import get_project_root

__all__ = ['from_root']


def from_root(
    *args: Iterable[str],
    create_parent_dirs=False,
    pathlib: bool = False,
) -> Union[str, Path]:
    """
    :param args:
    >>> from_root('dir1', 'dir2', 'dir3')
    <ROOT_DIR>/a/b/c
    :param create_parent_dirs:
        if the flag is set to True, all non-existing directories after <ROOT_DIR> will be created
    :param pathlib: whether or not to return `pathlib.Path` instead of `str`
    :return: `str` or `pathlib.Path`
    """
    args = map(str, args)
    path = get_project_root().joinpath(*args)

    if create_parent_dirs:
        _create_if_does_not_exist(path)

    if pathlib:
        path = Path(path)

    return path


def _create_if_does_not_exist(path: Path):
    if path.suffix:
        path = path.parent
    if not path.is_dir():
        path.mkdir(parents=True)
