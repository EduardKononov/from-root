from from_root import from_root
from pathlib import Path

path = from_root('a', 'b', 'c', 'file.txt', create_parent_dirs=True, return_type=Path)
with path.open('w') as file:
    file.write('from-root')
