import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        if not os.path.isfile("example.txt"):
            print("file not exist")
        else:
            return

    def __exit__(self, exc_type: str, exc_val: int, exc_tb: bool) -> None:
        os.remove(self.filename)
