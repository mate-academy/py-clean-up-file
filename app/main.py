import os

class CleanUpFile:
    def __init__(self, filename: str):
        self.filename = filename

    def __enter__(self):
        # Não precisamos fazer nada na entrada do contexto
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Remove o arquivo se ele existir
        if os.path.exists(self.filename):
            os.remove(self.filename)

