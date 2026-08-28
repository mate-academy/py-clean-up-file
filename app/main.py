import os


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type: BaseException | None,
                 exc_val: BaseException | None,
                 exc_tb: BaseException | None) -> None:
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            pass
        return
