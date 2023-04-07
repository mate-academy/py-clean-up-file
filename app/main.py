import os
from typing import Optional
from typing import Union


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(
            self,
            exc_type: Optional[type],
            exc_value: Optional[BaseException],
            tb: Union[type, None]
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)


with CleanUpFile("file.txt"):
    with open("file.txt", "w") as file:
        file.write("Hello Mate!")
