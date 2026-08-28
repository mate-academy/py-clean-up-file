import os
from typing import Type, Optional


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            traceback: Optional[Type[BaseException]]
    ) -> bool:
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"File {self.filename} has been removed.")
        else:
            print(f"File {self.filename} does not exist.")
        return True
