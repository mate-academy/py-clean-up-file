import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> None:
        self.file = open(self.filename)
        return self.file

    def __exit__(self,
                 exc_type: Any,
                 exc_value: Any,
                 exc_traceback: Any
                 ) -> None:
        self.file.close()
        self.__del__()

    def __del__(self) -> None:
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            print("File Not Found")
