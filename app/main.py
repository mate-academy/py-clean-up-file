import os
from typing import Self, Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)


with CleanUpFile("kex.txt"):
    with open("kex.txt", "w") as file:
        file.write("Hello Mate!")
