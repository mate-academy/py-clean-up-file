from os import remove


class CleanUpFile:
    def __init__(self, file_name: str) -> None:
        self.filename = file_name

    def __enter__(self) -> None:
        return self

    def __exit__(self, exit_type: type,
                 exit_value: Exception, exit_traceback: str) -> None:
        remove(self.filename)
