import os


class CleanUpFile:
    def __init__(self, name: str) -> None:
        self.name = name

    def __enter__(self) -> object:
        return self

    def __exit__(self) -> None:
        try:
            os.remove(self.name)
        except FileNotFoundError:
            pass
