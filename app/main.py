from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename: str = filename
        self.file = None

    def __enter__(self) -> CleanUpFile:
        self.file = open(self.filename, "w")
        return self

    def __exit__(self,
                 exc_type: type | None,
                 exc_val: BaseException | None,
                 exc_tb: object | None
                 ) -> None:
        self.file.close()
        try:
            os.remove(self.filename)
        except Exception as e_info:
            print("file now found", e_info)


with CleanUpFile("file.txt"):
    with open("file.txt", "w") as file:
        file.write("Hello Mate!")
