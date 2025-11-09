import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self._file = None

    def __enter__(self) -> "CleanUpFile":
        self._file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        self._file.close()
        if os.path.exists(self.filename):
            os.remove(self.filename)


with CleanUpFile("test.txt") as file:
    with open("file.txt", "w") as file:
        file.write("Hello Mate!")
