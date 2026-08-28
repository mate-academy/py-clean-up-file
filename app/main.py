import os
import typing


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self,
            exc_type: typing.Optional[type[BaseException]],
            exc_value: typing.Optional[BaseException],
            traceback: typing.Optional[object]) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
