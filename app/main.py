import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        try:
            with open(self.filename, "r"):
                pass
        except FileNotFoundError:
            pass
        else:
            os.remove(self.filename)
            print(f"The file '{self.filename}' has been removed.")
