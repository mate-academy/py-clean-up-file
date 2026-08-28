import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        # This method is called when entering the 'with' block.
        # You can optionally open the file here if needed.
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: object | None,
    ) -> None:
        # This method is called when exiting the 'with' block.
        # Remove the file if it exists.
        if os.path.exists(self.filename):
            os.remove(self.filename)
