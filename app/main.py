import os
from typing import Optional, Type, Tuple


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self,
                 exc_type: Type[BaseException],
                 exc_val: Optional[Type[BaseException]],
                 exc_tb: Optional[Tuple]
                 ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)


with CleanUpFile("filename") as manager:
    with open(manager.filename, "w") as f:
        f.write("Hello Mate!")

    with open(manager.filename, "r") as f:
        content = f.read()
        print(content)
