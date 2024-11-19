from os import remove, path

class CleanUpFile():
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, ext_type: str, value: str, traceback: str ) -> None:
        if path.exists(self.filename):
            remove(self.filename)
