from __future__ import annotations


class CleanUpFile:

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        return self

    def __exit__(self,
                 type_exc: BaseException,
                 value: BaseException,
                 traceback: BaseException) -> None:
        import os
        if os.path.exists(self.filename):
            os.remove(self.filename)
