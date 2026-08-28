import os


class CleanUpFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.filename.close()
        os.remove(self.filename)
