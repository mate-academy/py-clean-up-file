import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(
        self, exe_type: type, exe_value: Exception, traceback
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
