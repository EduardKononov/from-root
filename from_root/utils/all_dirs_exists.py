from pathlib import Path

__all__ = ['all_dirs_exists']


def all_dirs_exists(path: Path):
    if path.suffix:
        path = path.parent
    return path.is_dir()
