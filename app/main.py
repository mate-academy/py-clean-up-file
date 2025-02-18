import os
from typing import Optional, Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, "w")
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[object]
    ) -> None:
        self.file.close()
        if os.path.exists(self.filename):
            os.remove(self.filename)
        else:
            print(f"File {self.filename} doesn't exist!")
