class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type: str, exc_value: str, traceback: str) -> None:
        try:
            file_handle = open(self.filename, "r")
            file_handle.close()
            import os
        except FileNotFoundError:  # If the file doesn't exist
            return  # Nothing to clean up, exit early
        os.remove(self.filename)  # Remove the file
