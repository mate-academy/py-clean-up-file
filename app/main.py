from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: str) -> None:
        pass

    def __del__(self) -> None:
        os.remove(self.filename)


with CleanUpFile("file.txt"):
    with open("file.txt", "w") as file:
        file.write("Hello Mate!")
