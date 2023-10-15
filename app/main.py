from __future__ import annotations

import os


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self) -> None:
        os.remove(self.file_name)
