import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        try:
            if os.path.exists(self.filename):
                os.remove(self.filename)
                print(f"File {self.filename} has been removed.")
        except Exception as e:
            print(f"Error: {e}")
