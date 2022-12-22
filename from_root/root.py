from pathlib import Path

from from_root.get_project_root import get_project_root
from from_root.base import from_base

__all__ = ['from_root']


def from_root(*args: str) -> Path:
    """
    :param args:
    >>> from_root('dir1', 'dir2', 'file.txt')
    <ROOT_DIR>/dir1/dir2/file.txt
    :return: `pathlib.Path`
    """

    return from_base(
        args,
        base_path=get_project_root(),
    )


def main():
    print(from_root())


if __name__ == '__main__':
    main()
