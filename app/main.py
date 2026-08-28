from __future__ import annotations
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self,
            exc_type: Any,
            exc_value: Any,
            exc_traceback: Any
    ) -> None:
        import os
        if os.path.exists(self.filename):
            os.remove(self.filename)
