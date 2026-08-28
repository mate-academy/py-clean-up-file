from __future__ import annotations
import os
from typing import Any


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self, file_type: Any,
            file_value: Any, file_traceback: Any
    ) -> None:
        os.remove(self.filename)
