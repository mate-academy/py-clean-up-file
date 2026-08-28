import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> None:
        return self

    def __exit__(
            self,
            exc_type: str,
            exc_value: None,
            traceback: None
    ) -> None:
        pass

    def __del__(self) -> None:
        if os.path.isfile(self.filename):
            try:
                os.remove(self.filename)
            except Exception as e:
                print(e)
