import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(
            self,
            exception_type: Any,
            exception_value: Any,
            traceback: Any
    ) -> None:
        os.remove(self.filename)
