from pathlib import Path

from from_root.get_project_root import get_project_root
from from_root.base import from_base

__all__ = ['from_root']


def from_root(
        *args: str,
        mkdirs: bool = False,
) -> Path:
    """
    :param args:
    >>> from_root('dir1', 'dir2')
    <ROOT_DIR>/dir1/dir2
    :param mkdirs: if True, all non-existing names after <ROOT_DIR> will be created as directories
    :return: `pathlib.Path`
    """

    return from_base(
        args,
        mkdirs=mkdirs,
        base_path=get_project_root(),
    )


def main():
    print(from_root())


if __name__ == '__main__':
    main()
