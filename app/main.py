import os


class CleanUpFile:
    def __init__(self, filename: str) -> "CleanUpFile":
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exit_type: "CleanUpFile",
                 exit_value: "CleanUpFile",
                 traceback: "CleanUpFile") -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
