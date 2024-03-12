from __future__ import annotations

import os

from types import TracebackType


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(
            self,
            exc_type: type[BaseException] | None,
            exc_value: BaseException | None,
            exc_traceback: TracebackType | None
    ) -> None:
        pass

    def __del__(self) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
