import os
from typing import Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        print("Enter method called")
        return self

    def __exit__(
            self,
            exc_type: Type[BaseException],
            exc_val: BaseException,
            exc_tb: Type
    ) -> None:
        print("Exit method called")
        os.remove(self.filename)
