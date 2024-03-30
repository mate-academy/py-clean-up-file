import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file_obj = open(self.filename, "w")

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exc_type: None, exc_val: None, exc_tb: None) -> None:
        if self.file_obj:
            self.file_obj.close()
        if os.path.exists(self.filename):
            os.remove(self.filename)
        if exc_type is not None:
            pass
