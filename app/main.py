import os


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"File {self.filename} has been removed.")
        else:
            print(f"File {self.filename} does not exist.")
