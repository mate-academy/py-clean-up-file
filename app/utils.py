# app/utils.py

from __future__ import annotations

import os
from types import TracebackType
from typing import Optional, Type


class CleanUpFile:
    """Um gestor de contexto para apagar automaticamente um ficheiro à saída."""

    def __init__(self: CleanUpFile, filename: str) -> None:
        """
        Inicializa o gestor de contexto com o nome do ficheiro alvo.

        Args:
            filename: O caminho para o ficheiro a ser limpo.
        """
        self.filename = filename

    def __enter__(self: CleanUpFile) -> None:
        """
        Entra no contexto de execução.

        Este gestor de contexto não precisa de retornar um recurso específico,
        pelo que retorna None.
        """
        return None

    def __exit__(
        self: CleanUpFile,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        """
        Sai do contexto de execução e remove o ficheiro se ele existir.

        Este método trata da lógica de limpeza.
        """
        if os.path.exists(self.filename):
            os.remove(self.filename)
