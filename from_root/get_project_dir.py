import re
import traceback
from pathlib import Path

__all__ = ['get_project_root']


def get_project_root():
    stack = reversed(traceback.extract_stack())

    for frame in stack:
        try:
            path = Path(frame.filename).resolve()
        except OSError:
            # some frames have names that cannot be treated as file paths
            continue

        # packages installed using pip are stored in the 'site-packages'
        # if from_root is called from a package, we can quickly find the root directory
        posix_like = path.as_posix()
        if 'site-packages' in posix_like:
            root_path = Path(re.findall(r'.*site-packages/.*?/', posix_like)[0])
            # but we ignore 'from_root' package
            if root_path.name != 'from_root':
                return root_path

        while path.parents:
            if (
                (path / '.git').exists()
                or
                (path / '.project-root').exists()
            ):
                return path

            path = path.parent

    # TODO(ekon): put more details
    raise FileNotFoundError(
        f'There is neither ".git" directory nor ".project-root" file, '
        f'cannot detect root folder'
    )


if __name__ == '__main__':
    print(get_project_root())
