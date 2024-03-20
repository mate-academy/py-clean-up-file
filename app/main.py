from __future__ import annotations
from typing import Any
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
        self,
        ext_type: type,
        ext_value: Any,
        ext_traceback: Any
    ) -> None:
        os.remove(self.filename)
