import os


class CleanUpFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            with open(self.filename, 'r'):
                pass
        except FileNotFoundError:
            pass
        else:
            os.remove(self.filename)
            print(f"The file '{self.filename}' has been removed.")
      