from __future__ import annotations

import os.path


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, *args, **kwargs) -> None:
        os.remove(self.filename)
