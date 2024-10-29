import os


class CleanUpFile:
    def __init__(self, name: str) -> None:
        self.filename = name

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exc_type: type, exc_value: Exception,
                 exc_traceback: type) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
