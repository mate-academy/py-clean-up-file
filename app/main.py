import os
from typing import Any


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> None:
        return self

    def __exit__(self, exe_tp: Any, exe_val: Any, exe_tb: Any) -> None:
        os.remove(self.filename)
        return self
