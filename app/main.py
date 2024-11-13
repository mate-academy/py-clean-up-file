import os
from typing import Any


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def __enter__(self) -> Any:
        self.file = open(self.file_name, "w")
        return self.file_name

    def __exit__(self, exc_type: type, exc_val: str,
                 exc_tb: BaseException) -> None:
        self.file.close()
        os.remove(self.file_name)
