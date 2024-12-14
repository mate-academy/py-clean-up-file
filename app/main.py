from os import path, remove
from typing import Optional, Type, Any


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> None:
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            traceback: Optional[Any]
    ) -> None:
        if path.exists(self.filename):
            remove(self.filename)
