import warnings
from pathlib import Path
from typing import Iterable

from from_root.utils import all_dirs_exists

__all__ = ['from_base']


def from_base(args: Iterable[str], mkdirs: bool, base_path: Path):
    path = base_path.joinpath(*args)

    if not all_dirs_exists(path):
        if mkdirs:
            path.mkdir(parents=True)
        else:
            # TODO(ekon): add global disabling of the message
            warnings.warn(f'{path} has non-existing directories. Consider setting `mkdirs=True`')

    return path
