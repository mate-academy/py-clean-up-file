from os import remove, path


class CleanUpFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if path.exists(self.filename):
            remove(self.filename)
