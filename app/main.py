from os import remove


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> CleanUpFile:
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: Exception, exc_val: str, exc_tb: str) -> None:
        self.file.close()
        remove(self.filename)
