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
            exc_type: type | None,
            exc_val: Exception | None,
            exc_traceback: Any | None
    ) -> None:
        os.remove(self.filename)
