import os


class CleanUpFile():
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        self.f = open(self.filename, "w")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        try:
            self.f.close()
        except FileNotFoundError:
            pass
        os.remove(self.filename)
