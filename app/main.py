from __future__ import annotations
from typing import Any

import os


class CleanUpFile:
    def __init__(self, filenamae: str) -> None:
        self.filename = filenamae

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self,
            exc_type: Any,
            exc_value: Any,
            exc_traceback: Any
    ) -> None:
        os.remove(self.filename)
