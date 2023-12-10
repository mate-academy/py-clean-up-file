import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.mode = "w"
        self.file = None

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, self.mode)
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self.file.close()
        os.remove(self.filename)
