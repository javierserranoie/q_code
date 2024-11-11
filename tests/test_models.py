import unittest

from q_code_game.models import QCode


class TestSettings(unittest.TestCase):
    def test_default(self):
        element = QCode(
            code="QSL", question="Puede confirmarme recibo?", answer="Confirmo recibo"
        )

        assert element.code == "QSL"
