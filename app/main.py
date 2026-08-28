import os


class CleanUpFile:
    def __init__(self, filename: None) -> None:
        self.filename = filename

    def __enter__(self: object) -> object:

        return self

    def __exit__(self, exc_type: object, exc_value: object,
                 traceback: object) -> None:

        if os.path.exists(self.filename):

            os.remove(self.filename)
