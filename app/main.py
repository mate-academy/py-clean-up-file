import os
from types import TracebackType
from typing import Optional, Type


class CleanUpFile:
    """Um gerenciador de contexto para remover um arquivo após o uso."""

    def __init__(self, filename: str) -> None:
        self.filename: str = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)


# Exemplo de uso:
with CleanUpFile("file.txt"):
    with open("file.txt", "w", encoding="utf-8") as file:
        file.write("Hello Mate!")
