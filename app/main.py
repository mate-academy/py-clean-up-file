class CleanUpFile:
    def __init__(name: str) -> None:
        self.name = name
    
    def __enter__(self):
        pass

    def __exit__(self):
        pass
    
    def __del__(self):
        del(self.name)
      