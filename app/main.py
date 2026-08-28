import os
from typing import Optional, Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> "CleanUpFile":
        try:
            if not os.path.exists(self.filename):
                open(self.filename, "w").close()

            self.file = open(self.filename, "r+")
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' does not exist.")
            raise
        except PermissionError:
            print(f"Error: Permission denied for file '{self.filename}'.")
            raise
        except IOError as e:
            print(f"An I/O error occurred: {e}")
            raise
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[object]) -> None:
        try:
            if self.file:
                self.file.close()
            if os.path.exists(self.filename):
                os.remove(self.filename)
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' "
                  f"was not found during deletion.")
        except PermissionError:
            print(f"Error: Permission denied when "
                  f"trying to delete '{self.filename}'.")
        except IOError as e:
            print(f"An I/O error occurred while deleting the file: {e}")
