from typing import Optional, Type, Any, Union
from pathlib import Path
import types


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_value: Optional[BaseException],
                 traceback: Optional[Union[types.TracebackType, Any]]) -> None:
        file_path = Path(self.filename)
        if file_path.exists():
            file_path.unlink()
