from pathlib import Path

__all__ = [
    'CONFIG',
    'raise_on_wrong_return_type',
]


def raise_on_wrong_return_type(return_type):
    if return_type not in (str, Path):
        raise ValueError(f'Return type must be `str` or `pathlib.Path`, got {type(return_type)}')


class _Config:
    def __init__(self):
        self._default_return_type = str

    @property
    def default_return_type(self):
        return self._default_return_type

    @default_return_type.setter
    def default_return_type(self, return_type):
        raise_on_wrong_return_type(return_type)
        self._default_return_type = return_type


CONFIG = _Config()
