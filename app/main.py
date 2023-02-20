import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        try:
            os.path.exists(self.filename)
        except Exception as e:
            print(f"The exception {e} was occurred")
        finally:
            os.remove(self.filename)

            print(f"{self.filename} was removed")
