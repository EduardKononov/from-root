from pathlib import Path
from typing import Iterable, Union

from from_root.get_project_dir import get_project_dir
from from_root.config import CONFIG, raise_on_wrong_return_type

__all__ = ['from_root']


def from_root(
    *args: Iterable[str],
    create_parent_dirs=False,
    return_type=None,
) -> Union[str, Path]:
    """
    :param args:
    >>> from_root('a', 'b', 'c')
    <ROOT_DIR>/a/b/c
    :param create_parent_dirs:
        if the flag is set to True, all non-existing directories after <ROOT_DIR> will be created
    :param return_type: `str` or `pathlib.Path`. If not `None`, `CONFIG.default_return_type` is used
    :return: `str` or `pathlib.Path`
    """
    if return_type is None:
        return_type = CONFIG.default_return_type
    else:
        raise_on_wrong_return_type(return_type)

    args = map(str, args)
    path = get_project_dir().joinpath(*args)

    if create_parent_dirs:
        _create_if_does_not_exist(path)

    path = return_type(path)

    return path


def _create_if_does_not_exist(path: Path):
    if path.suffix:
        path = path.parent
    if not path.is_dir():
        path.mkdir(parents=True)
