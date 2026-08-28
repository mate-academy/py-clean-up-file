from __future__ import annotations
import os
import typing


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: typing.Optional[typing.Type[BaseException]],
                 exc_val: typing.Optional[BaseException],
                 exc_tb: typing.Optional[typing.Any]) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)


with CleanUpFile("file.txt"):
    with open("file.txt", "w") as file:
        file.write("Hello Mate!")
