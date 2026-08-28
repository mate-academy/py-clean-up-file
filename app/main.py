import os
import types


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self,
                 exc_type: type[BaseException] | None,
                 exc_value: BaseException | None,
                 traceback: types.TracebackType | None) -> None:
        os.remove(self.filename)
