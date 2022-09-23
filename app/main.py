import os


class CleanUpFile:

    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, e_type, e_value, e_traceback):
        self.file.close()
        os.remove(self.filename)
