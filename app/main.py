from os import remove
from typing import Optional, Type


class CleanUpFile:
    def __init__(self, name: str) -> None:
        self.filename = name

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[Type[BaseException]],
                 exc_tb: Optional[object]) -> None:
        remove(self.filename)
