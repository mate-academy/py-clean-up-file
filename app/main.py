import os


class CleanUpFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type=None, exc_val=None, exc_tb=None):
        if self.file:
            self.file.close()
        if os.path.exists(self.filename):
            os.remove(self.filename)
