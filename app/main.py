from typing import Generator, Optional, Type
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> Generator:
        return self

    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[Type[BaseException]]) -> None:
        path = os.path.abspath(self.filename)
        os.remove(path)
