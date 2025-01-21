import os
from typing import Optional, Type, Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_value: Optional[BaseException],
                 traceback: Optional[Any]) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)


# Example usage
if __name__ == "__main__":
    with CleanUpFile("file.txt"):
        with open("file.txt", "w") as file:
            file.write("Hello Mate!")
