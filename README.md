# Usage guide

Are you fed up with that **annoying FileNotFoundError** when your working directory turns out to be something different
from what you expected? Or, maybe, you are looking for an easy and robust way of declaring paths to configs and any data
files in your project? We have got a solution, keep reading.

The package is really tiny, there are two function:

* `from_root` helps with declaring absolute paths relative to your project root
* `from_here` comes in handy when you want to declare a path relative to the current file

They are dead simple to use.

Let's assume we have a project with the next structure:

```
├── .git  # OPTIONAL. See explanation below
├── .project-root  # OPTIONAL. See explanation below
├── config.json  
├── assets  
│ ├── animation.gif  
│ └── logo.png  
└── package  
    ├── __init__.py
    ├── data.csv    
    ├── script.py
    ├── FROM_HERE_DEMO.py
    └── inner_package  
      ├── FROM_ROOT_DEMO.py  
      ├── __init__.py
      └── insanely
          └── deep
              └── dir
                  └── file.txt
```

#### `from_root` examples:

```python
# <PROJECT_ROOT>/package/inner_package/FROM_ROOT_DEMO.py
from from_root import from_root

CONFIG_PATH = from_root('config.json')

PACKAGE_DATA_PATH = from_root('package', 'data.csv')

# `from_root` returns pathlib.Path object
# so we can take advantage of its fantastic "/" syntax
ASSETS_DIR = from_root('assets')
ANIMATION_PATH = ASSETS_DIR / 'animation.gif'
LOGO_PATH = ASSETS_DIR / 'logo.png'

# no matter how deep it's located
FILE_TXT_PATH = from_root('package', 'inner_package', 'insanely', 'deep', 'dir', 'file.txt')

# assume you have stuff to save in a separate directory that does not exist yet.
# If `mkdirs` is set to True (False by default), all the non existing directories in the path 
# will be created before `from_root` returns. If a directory already exists, nothing happens

import pickle

RESULTS_DIR = from_root('package', 'deep', 'results', 'dir', mkdirs=True)
results = {
    'ones': [1, 1, 1],
    'zeros': [2, 2, 2]
}
for name, data in results.items():
    path = RESULTS_DIR / f'{name}.pkl'
    # `FileNotFoundError` is not raised because `from_root` has created all non-existing directories
    with path.open('wb') as file:
        pickle.dump(data, file)
```

#### `from_here` examples:

```python
# <PROJECT_ROOT>/package/FROM_HERE_DEMO.py
from from_root import from_here

# The only difference from `from_root` is that `from_here` allows you to declare relative paths
# I think the examples speaks for themselves quite good. 
# Take a look at tree above and compare with `from_root` examples

CONFIG_PATH = from_here('data.csv')
FILE_TXT_PATH = from_here('inner_package', 'insanely', 'deep', 'dir', 'file.txt')
```

# How does it work?

When `from_root` is called, folders in the current traceback are looked through one by one in order to find `.git`
directory or `.project-root` file (might be empty; you have to create it on your own). The first one that contains at
least one of them are considered as a root directory.

There is a special case. If your package was installed by someone else via, for example, `pip`, the root directory is
the one that is next to `site-packages` so there will be no conflicts with your usages of from-root and your users' ones
