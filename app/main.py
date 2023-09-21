import os


class CleanUpFile:
    def __init__(self, name: str) -> None:
        self.name = name

    def __enter__(self) -> object:
        return self

    def __exit__(self,
                 exc_type: Any,
                 exc_val: Any,
                 exc_tb: Any) -> None:
        try:
            os.remove(self.name)
        except FileNotFoundError:
            pass
