import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.file_name = filename
        self.file_obj = open(self.file_name)

    def __enter__(self) -> Any:
        return self.file_obj

    def __exit__(self, exc_type: Any,
                 exc_val: Any,
                 exc_tb: Any) -> None:
        self.file_obj.close()
        os.remove(self.file_name)
