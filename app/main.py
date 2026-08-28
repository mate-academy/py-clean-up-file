from os import remove


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.file = open(filename, "w")
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exc_type: None, exc_val: None, exc_tb: None) -> None:
        self.file.close()
        remove(self.filename)
