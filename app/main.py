import os
from typing import Optional


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self,
            exc_type: Optional[bool],
            exc_val: Optional[bool],
            exc_tb: Optional[bool]) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)


with CleanUpFile("file.txt") as cleanup_obj:
    with open(cleanup_obj.filename, "w") as file:
        file.write("Hello Mate!")
