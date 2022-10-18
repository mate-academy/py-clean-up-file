import os


class CleanUpFile(object):
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        os.remove(self.filename)




