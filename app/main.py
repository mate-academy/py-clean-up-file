import os


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type: str, exc_val: str, traceback: str) -> None:
        os.remove(self.file_name)
