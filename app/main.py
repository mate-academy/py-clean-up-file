from typing import Optional, Type, TypeVar

T = TypeVar("T", bound="CleanUpFile")


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> T:
        return self  # Returns an instance of CleanUpFile or its subclass

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[object]
    ) -> None:
        import os
        if os.path.exists(self.filename):
            os.remove(self.filename)
