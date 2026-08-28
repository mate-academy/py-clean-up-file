import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        open(self.filename, "a").close()
        return self

    def __exit__(self, exc_type: type, exc_val: Exception,
                 exc_tb: Exception) -> None:
        if os.path.isfile(self.filename):
            os.remove(self.filename)
