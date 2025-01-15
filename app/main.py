import os


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exc_type: type, exc_value:
                 Exception, traceback: object) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"File {self.filename} has been removed.")
        else:
            print(f"File {self.filename} does not exist.")
