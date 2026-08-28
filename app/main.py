import os
import traceback
from typing import Optional, Type


class CleanUpFile:
    def __init__(
            self, filename: str
    ) -> None:
        self.filename = filename

    def __enter__(
            self
    ) -> "CleanUpFile":
        self.file = open(self.filename, "w")
        return self

    def __exit__(
            self, exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: traceback
    ) -> None:
        self.file.close()
        os.remove(self.filename)


with CleanUpFile("file.txt") as file:
    file.file.write("Hello Mate!")
