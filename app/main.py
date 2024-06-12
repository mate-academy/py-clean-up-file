import os


class CleanUpFile:
    def __init__(self, filename: str, method: str = "w") -> None:
        self.filename = filename
        self.method = method
        self.file = None

    def __enter__(self) -> None:
        self.file = open(self.filename, self.method)
        return self

    def __exit__(self, type_file: str, value: str, traceback: str) -> None:
        self.file.close()
        try:
            os.remove(self.filename)
        except OSError:
            print("File does not exists")
