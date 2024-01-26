class CleanUpFile:
    def __init__(self, file_name: str, method: str) -> None:
        self.file_obj: TextIO = open(file_name, method)
        
    def __enter__(self) -> TextIO:
        return self.file_obj
        
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.file_obj.close()
