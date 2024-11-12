import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        # Enter the context without performing any actions on the file
        return self

    def __exit__(self, exc_type: None, exc_val: None, exc_tb: None) -> None:
        # Remove the file if it exists after exiting the context
        if os.path.exists(self.filename):
            os.remove(self.filename)
