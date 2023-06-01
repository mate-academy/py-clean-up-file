from os import remove


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(self, *args) -> None:
        try:
            remove(self.filename)
        except OSError:
            return
