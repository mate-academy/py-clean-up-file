from typing import Any
import os


class CleanUpFile:
    # write your code here
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Any:
        return self

    def __exit__(self, *args: Any) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
        self.__del__()

    def __del__(self) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
