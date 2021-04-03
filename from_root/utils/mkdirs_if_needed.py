from pathlib import Path

__all__ = ['mkdirs_if_needed']


def mkdirs_if_needed(path: Path):
    if path.suffix:
        path = path.parent
    if not path.is_dir():
        path.mkdir(parents=True)
