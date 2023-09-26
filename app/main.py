import os


class CleanUpFile:
    # write your code here
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> callable:
        return self

    def __exit__(self, types : None, value : None, traceback: None) -> None:
        os.remove(self.filename)
