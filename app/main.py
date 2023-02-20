import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(
            self,
            exception_type: BaseException | None,
            exception_value: BaseException | None,
            traceback: any
    ) -> None:
        os.remove(self.filename)
