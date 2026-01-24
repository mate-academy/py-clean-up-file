import os
from typing import Any


class CleanUpFile:
    def __init__(self, filename:str):
        self.filename = filename    
    
    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exit_type, exit_value, traceback) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
