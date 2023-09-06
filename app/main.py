import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(self, ab: str, bc: str, cd: str) -> None:
        os.remove(self.filename)
