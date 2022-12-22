import traceback
from pathlib import Path
from typing import Tuple

__all__ = ['get_project_root']

ANCHORS = ('.git', '.project-root')


def get_project_root():
    py_paths = _extract_py_files_from_traceback()

    for path in py_paths:
        path = path.parent

        while path.parents:
            if _has_anchor(path):
                return path

            path = path.parent

    # TODO(ekon): put more details
    # TODO(ekon): add warning about relying on ".git"
    raise FileNotFoundError(
        f'No possible anchors found ({", ".join(ANCHORS)}), cannot detect root folder. '
        'Initialize a git repository or create an empty ".project-root" file '
        'in the project root'
    )


def _extract_py_files_from_traceback() -> Tuple[Path]:
    stack = reversed(traceback.extract_stack())
    file_names = (
        frame.filename
        for frame in stack
    )
    py_files_paths = (
        Path(filename).resolve()
        for filename in file_names
        if filename.endswith('.py')
    )
    return tuple(py_files_paths)


def _has_anchor(path: Path) -> bool:
    for name in ANCHORS:
        if (path / name).exists():
            return True
    return False
