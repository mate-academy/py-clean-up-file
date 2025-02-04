import os


class CleanUpFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
