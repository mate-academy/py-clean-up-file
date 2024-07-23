import os
from typing import Optional, Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self, exc_type: Optional[Type[BaseException]],
            exc_val: Optional[Type[BaseException]],
            exc_tb: Optional[Type[BaseException]]
    ) -> bool:
        if os.path.exists(self.filename):
            os.remove(self.filename)
        return False


with CleanUpFile("file.txt") as clean_up:
    with open(clean_up.filename, "w") as file:
        file.write("Hello Mate!")
