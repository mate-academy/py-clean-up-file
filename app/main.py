import os


class CleanUpFile:
    # write your code here
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(
            self,
            exc_type: BaseException,
            exc_val: BaseException,
            exc_tb: BaseException
    ) -> None:
        os.remove(self.filename)
