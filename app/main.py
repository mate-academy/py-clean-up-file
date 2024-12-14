import os.path


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
            print(f"File '{self.file_name}' has been deleted.")
