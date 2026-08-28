from __future__ import annotations

import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> CleanUpFile:
        with open(self.filename, "w") as f:
            f.write("test")
        return self

    def __exit__(self, exc_type: type, exc_val: type, exc_tb: type) -> None:
        os.remove(self.filename)
