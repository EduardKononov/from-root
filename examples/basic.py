from from_root import from_root

path = from_root('a', 'b', 'c', 'file.txt', create_parent_dirs=True, pathlib=True)
with path.open('w') as file:
    file.write('from-root')
