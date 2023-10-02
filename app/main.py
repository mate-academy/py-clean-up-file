class CleanUpFile:
    def __init__(file_name: str, method: str) -> None:
        self.file_obj = open(file_name, method)
    
    def __enter__(self):
        return self.file_obj

    def __exit__(self):
        self.file_obj.close()
    
    def __del__(self):
        del(self.file_obj)
      