from pathlib import Path
from typing import Iterable

__all__ = ['from_base']


def from_base(args: Iterable[str], base_path: Path):
    path = base_path.joinpath(*args)

    return path
