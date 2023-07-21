from __future__ import annotations

import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, type_: Any,
                 value: Any, traceback: Exception) -> None:
        try:
            os.remove(self.filename)
        except traceback as clean_exception:
            raise clean_exception
