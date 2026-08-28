import os
from typing import Any
from types import TracebackType


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Any:
        try:
            self.file = open(self.filename, "r")
            return self.file
        except FileNotFoundError as e:
            print(f"didko, something went wrong! {e}")
        return self

    def __exit__(
            self,
            exc_type: type[BaseException],
            exc_val: BaseException,
            exc_tb: TracebackType,) -> Any:
        if exc_type:
            if issubclass(exc_type, FileNotFoundError):
                print(f"didko, something went wrong! {exc_val}")
                return True
        if os.path.exists(f"{self.filename}"):
            os.remove(self.filename)
