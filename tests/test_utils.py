# tests/test_utils.py

import os
import unittest

from app.utils import CleanUpFile


class TestCleanUpFile(unittest.TestCase):
    """Testes para o gestor de contexto CleanUpFile."""

    def setUp(self):
        """Configura um nome de ficheiro temporário para os testes."""
        self.test_file = "test_file_for_cleanup.txt"

    def tearDown(self):
        """Garante que o ficheiro de teste é removido após cada teste."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_file_is_removed_on_successful_exit(self):
        """Verifica se o ficheiro é apagado após o bloco 'with' sair normalmente."""
        with CleanUpFile(self.test_file):
            with open(self.test_file, "w") as f:
                f.write("This is a test.")
            # Dentro do contexto, o ficheiro deve existir
            self.assertTrue(os.path.exists(self.test_file))

        # Fora do contexto, o ficheiro não deve existir
        self.assertFalse(os.path.exists(self.test_file))

    def test_file_is_removed_on_exception(self):
        """Verifica se o ficheiro é apagado mesmo que ocorra uma exceção."""
        with self.assertRaises(ValueError):
            with CleanUpFile(self.test_file):
                with open(self.test_file, "w") as f:
                    f.write("This file should also be cleaned up.")
                self.assertTrue(os.path.exists(self.test_file))
                raise ValueError("Simulating an error.")

        # Mesmo após a exceção, o ficheiro deve ter sido removido
        self.assertFalse(os.path.exists(self.test_file))

    def test_no_error_if_file_not_created(self):
        """Verifica que não ocorre erro se o contexto sair antes da criação do ficheiro."""
        try:
            with CleanUpFile(self.test_file):
                # O ficheiro nunca é criado neste bloco.
                pass
        except FileNotFoundError:
            self.fail("CleanUpFile levantou FileNotFoundError inesperadamente.")

        self.assertFalse(os.path.exists(self.test_file))
