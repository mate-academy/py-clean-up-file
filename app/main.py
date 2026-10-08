from os import remove


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self, exc_type: None, exc_val: None, exc_tb: None) -> None:
        if open(self.filename):
            remove(self.filename)
