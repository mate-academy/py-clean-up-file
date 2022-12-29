import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str, mode: str = "w") -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self) -> Any:
        self.file = open(self.filename, self.mode)
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.file.close()
        os.remove("file.txt")


with CleanUpFile("file.txt"):
    with open("file.txt", "w") as file:
        file.write("Hello mate")
