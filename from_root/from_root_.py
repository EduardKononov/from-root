from pathlib import Path

from from_root.utils import mkdirs_if_needed, get_project_root

__all__ = ['from_root']


def from_root(*args: str, mkdirs=False) -> Path:
    """
    :param args:
    >>> from_root('dir1', 'dir2', 'file.txt')
    <ROOT_DIR>/dir1/dir2/file.txt
    :param mkdirs: if True, all non-existing directories after <ROOT_DIR> will be created
    :return: `pathlib.Path`
    """

    path = get_project_root().joinpath(*args)

    if mkdirs:
        mkdirs_if_needed(path)

    return path


def main():
    print(from_root())


if __name__ == '__main__':
    main()
