import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> any:
        return self

    def __exit__(self, exc_type: any, exc_value: any, traceback: any) -> None:
        try:
            os.remove(self.filename)
        except Exception as e:
            print(e)
