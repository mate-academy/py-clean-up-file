class CleanUpFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            with open(self.filename, 'r'):
                pass
            if exc_type is None:
                self._remove_file()
        except FileNotFoundError:
            pass

    def _remove_file(self):
        with open(self.filename, 'w'):
            pass
        print(f"The file '{self.filename}' has been removed.")
