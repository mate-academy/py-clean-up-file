from typing import Any
import os


class CleanUpFile:
    def __init__(self, filename) -> None:
        self.filename = filename


    def __enter__(self) -> Any:
        return self


    def __exit__(self, exc_type, exc_value, exc_traceback) -> Any:
        if os.path.exists(self.filename):
            os.remove(self.filename)