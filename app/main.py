import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename: str = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self,
                 exc_type: None,
                 exc_value: None,
                 traceback: None) -> bool:
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"File {self.filename} deleted.")
        return False
