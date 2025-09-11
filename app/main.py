import os


class CleanUpFile:
    def __init__(self, filename: str, open_type: str = "w") -> any:
        self.filename = filename
        self.open_type = open_type
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass
