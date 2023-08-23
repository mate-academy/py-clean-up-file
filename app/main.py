import os
from types import TracebackType
from typing import Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_value: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool:
        if os.path.exists(self.filename):
            try:
                os.remove(self.filename)
            except OSError as e:
                print(f"Cannot remove {self.filename}: {e}")
        return False
