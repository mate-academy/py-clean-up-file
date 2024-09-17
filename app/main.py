import os


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> None:
        return self

    def __exit__(self, typo: str, value: str, traceback: str) -> None:
        os.remove(self.filename)
