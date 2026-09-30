import os
from typing import TextIO


class CleanUpFile:
    def __init__(self, name: str) -> None:
        self.filename: str = name
        self.file: TextIO | None = None

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, "w")
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        exc_traceback: object | None,
    ) -> None:
        print("exit method called")

        if self.file is not None:
            self.file.close()

        os.remove(self.filename)
