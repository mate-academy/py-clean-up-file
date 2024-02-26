class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type: str) -> None:
        try:
            with open(self.filename, "r"):
                pass
            if exc_type is None:
                self._remove_file()
        except FileNotFoundError:
            pass

    def _remove_file(self) -> None:
        with open(self.filename, "w"):
            pass
