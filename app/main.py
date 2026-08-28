from os import remove, path


class Clean:
    pass


class CleanUpFile(Clean):
    def __init__(self, filename: str) -> None:
        self.filename = filename

    # How to set self annotation? When i set CleanUpFile python raise NameError
    def __enter__(self) -> Clean:
        return self

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str) -> None:
        if path.exists(self.filename):
            remove(self.filename)
