import re
import traceback
from pathlib import Path, PureWindowsPath
from typing import Tuple

__all__ = ['get_project_root']


def get_project_root():
    py_paths = _extract_py_files_from_traceback()

    for path in py_paths:
        path = path.parent

        # packages installed using pip are stored in the 'site-packages'
        site_package_dir = _handle_site_packages(path)
        if site_package_dir is not None:
            return site_package_dir

        while path.parents:
            if _has_anchor(path):
                return path

            path = path.parent

    # TODO(ekon): put more details
    raise FileNotFoundError(
        f'There is neither ".git" directory nor ".project-root" file, '
        f'cannot detect root folder. Initialize a git repository or create an empty ".project-root" file '
        f'in the project root'
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


def _handle_site_packages(path: Path):
    str_path = str(path)
    if isinstance(path, PureWindowsPath):
        str_path = str_path.replace('\\', '/')
    if 'site-packages' in str_path:
        # tested agains:
        # /python/site-packages/package
        # /python/site-packages/site-packages/package/whatever
        # /python/site-packages/package/

        regex = r'.*?site-packages/.*?[^/\n]*'

        site_package_regex = re.compile(regex)
        site_package_candidates = site_package_regex.findall(str_path)
        site_package_path = site_package_candidates[0]
        root_path = type(path)(site_package_path)

        if root_path.name != 'from_root':
            return root_path


def _has_anchor(path: Path) -> bool:
    for name in ('.git', '.project-root'):
        if (path / name).exists():
            return True
    return False
