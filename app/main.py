import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> object:
        return self

    def __exit__(self, exc_type: any, exc_val: any, exc_tb: any) -> None:
        try:
            os.remove(self.filename)
        except FileNotFoundError:
            print(f"Error: file {self.filename} not exist")
        except PermissionError:
            print(f"Error: insufficient permissions "
                  f"to delete {self.filename}.")
        except Exception as e:
            print(f"Unexpected error while deleting {self.filename}: {e}")
