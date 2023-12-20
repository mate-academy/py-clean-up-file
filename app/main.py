import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(self, *args) -> None:
        try:
            os.remove(self.filename)
        except FileNotFoundError as error:
            print(error, "error in manager")
            return None
