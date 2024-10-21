import os


class CleanUpFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

        if os.path.exists(self.filename):
            os.remove(self.filename)

