from typing import Any, Type
from os import path, remove


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Any:
        return self

    def __exit__(
            self,
            exc_type: Type[BaseException],
            exc_val: BaseException,
            exc_tb: Any
    ) -> None:
        if path.exists(self.filename):
            remove(self.filename)
