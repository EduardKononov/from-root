import traceback
from pathlib import Path

from from_root.utils import mkdirs_if_needed

__all__ = ['from_here']


def from_here(*args: str, mkdirs=False) -> Path:
    """
    :param args:
    >>> from_here('dir1', 'dir2', 'file.txt')
    <DIRECTORY_WHERE_THIS_FUNCTION_WAS_CALLED>/dir1/dir2/file.txt
    :param mkdirs:
        if True, all non-existing directories after <DIRECTORY_WHERE_THIS_FUNCTION_WAS_CALLED> will be created
    :return: `pathlib.Path`
    """

    here_dir = Path(traceback.extract_stack()[-2].filename).parent
    path = here_dir.joinpath(*args)

    if mkdirs:
        mkdirs_if_needed(path)

    return path


def main():
    print(from_here())


if __name__ == '__main__':
    main()
