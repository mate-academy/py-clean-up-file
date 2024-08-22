from __future__ import annotations

from os import remove, path


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, *args, **kwargs) -> None:
        if path.isfile(self.filename):
            remove(self.filename)
