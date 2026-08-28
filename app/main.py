import os
from typing import Any


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> None:
        return self

    def __exit__(self,
                 exc_type: Any, exc_value: Any,
                 exc_traceback: Any
                 ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)


with CleanUpFile("file.txt") as cleaner:
    with open("file.txt", "w") as file:
        file.write("Hello Mate!")
