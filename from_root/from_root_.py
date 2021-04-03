from pathlib import Path

from from_root.utils import get_project_root
from from_root.from_base import from_base

__all__ = ['from_root']


def from_root(*args: str, mkdirs=False) -> Path:
    """
    :param args:
    >>> from_root('dir1', 'dir2', 'file.txt')
    <ROOT_DIR>/dir1/dir2/file.txt
    :param mkdirs: if True, all non-existing directories after <ROOT_DIR> will be created
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
