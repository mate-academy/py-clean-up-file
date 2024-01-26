from typing import TextIO, Optional


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename: str = filename

    def __enter__(self) -> TextIO:
        return self

    def __exit__(
        self,
        exc_type: Optional,
        exc_value: Optional,
        traceback: Optional
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"The file '{self.filename}' has been removed.")
