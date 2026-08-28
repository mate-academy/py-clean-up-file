import os.path


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(self, typ: object, value: object,
                 traceback: object) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
