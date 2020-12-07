import re
import traceback
from pathlib import Path

__all__ = ['get_project_dir']


def get_project_dir():
    stack = reversed(traceback.extract_stack())
    the_most_recent = next(stack)
    file_path = Path(the_most_recent.filename).resolve()

    # packages installed using pip are stored in the 'site-packages'
    # if from_root is called from a package, we can quickly find the root
    if 'site-packages' in file_path.as_posix():
        return Path(re.findall(r'.*site-packages/.*?/', file_path.as_posix())[0])

    path = file_path.parent
    while path.parents:
        if (
            (path / '.git').exists()
            or
            (path / '.project-root').exists()
        ):
            return path

        path = path.parent

    # TODO(ekon): put more details
    raise FileExistsError(
        f'There is neither ".git" directory nor ".project-root" file — '
        f'impossible to detect root folder'
    )


if __name__ == '__main__':
    print(get_project_dir())
