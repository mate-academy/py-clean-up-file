import os
from types import TracebackType
from typing import Optional, Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None
        print("init method called")

    def __enter__(self) -> object:
        self.file = open(self.filename, "w")
        print("enter method called")
        return self

    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[TracebackType]
                 ) -> None:
        print("exit method called")
        self.file.close()
        os.remove(self.filename)


with CleanUpFile("file.txt"):
    with open("file.txt", "w") as manger:
        manger.write("Hello Mate!")
