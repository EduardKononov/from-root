from pathlib import Path
from typing import Iterable

__all__ = ['from_base']


def from_base(
        args: Iterable[str],
        base_path: Path,
        mkdirs: bool = False
):
    path = base_path.joinpath(*args)

    if mkdirs:
        try:
            path.mkdir(parents=True)
        except FileExistsError:
            pass

    return path
