# Motivation
TODO

# Usage guide
You can execute the code below from any script of your project, no matter how deep it is located.
The library automatically detects the project root. When `from_root` is called, 
all the folders in traceback are looked through in order to find `.git` directory or 
`.project-root` file (might be empty; you have to create it on your own). 
The first one that contains at least one of them are considered as root directory

There is a special case. If your package was installed by someone else using, for example, `pip`, the root directory is
the one that is next to `site-packages` directory.

The information about `from_root` parameters can be found in its docstring (`from_root.__doc__`) 

```python
from from_root import from_root

path = from_root('a', 'b', 'c', 'file.txt', create_parent_dirs=True, pathlib=True)
with path.open('w') as file:
    file.write('from-root')
```
