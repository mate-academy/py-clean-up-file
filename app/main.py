import os


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def __enter__(self) -> None:
        open(self.file_name, "a").close()

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
            print(f"Delete file: {self.file_name}")
        return False
