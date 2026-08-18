import os


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def __enter__(self) -> None:
        open(self.file_name, "a").close()

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if os.path.exists(self.sciezka):
            os.remove(self.sciezka)
            print(f"Delete file: {self.sciezka}")
        return False
