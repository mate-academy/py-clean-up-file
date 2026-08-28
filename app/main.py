import os
from typing import Optional, Any


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, "w")
        return self

    def __exit__(self,
                 exc_type: Optional[type],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[Any]
                 ) -> None:
        self.file.close()
        if os.path.exists(self.filename):
            os.remove(self.filename)

        return False


if __name__ == "__main__":
    with CleanUpFile("test.txt") as cleanup:
        cleanup.file.write("This is a test.")
