from os import remove, path


class CleanUpFile:
    def __init__(self, filename) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if path.exists(self.filename):
            remove(self.filename)
