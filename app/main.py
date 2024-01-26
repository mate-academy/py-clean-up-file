from typing import TextIO, Optional


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.file_obj: = open(filename)

    def __enter__(self) -> TextIO:
        return self.file_obj

    def __exit__(
        self,
        exc_type: Optional,
        exc_value: Optional,
        traceback: Optional
    ) -> None:
        self.file_obj.close()
