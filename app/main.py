import os


class CleanUpFile:
    def __init__(self, name) -> None:
        self.name = name

    def __enter__(self) -> None:
        self.name = open(self.name)
        return self.name

    def __exit__(self) -> None:
        os.remove(self.name)
