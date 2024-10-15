import os.path


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:  # noqa
        if os.path.exists(self.filename):
            os.remove(self.filename)
