import unittest
import parameterized as parameterized
from src import ConvertisseurNombresRomains


class MyTestCase(unittest.TestCase):

    @parameterized.parameterized.expand([[1], [2], [3]])
    def test_one_to_three(self, nombre):
        # ETANT DONNE un chiffre entre 1 et 3
        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(nombre)

        # ALORS on obtient <n> fois 'I'
        attendu = 'I' * nombre
        self.assertEqual(attendu, result)

    def test_four(self):
        # ETANT DONNE le chiffre 4
        nombre = 4

        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(nombre)

        # ALORS on obtient 'IV'
        self.assertEqual('IV', result)

    @parameterized.parameterized.expand([[5], [6], [7], [8]])
    def test_five_to_eight(self, nombre):
        # ETANT DONNE un chiffre entre 5 et 8
        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(nombre)

        # ALORS on obtient 'V' + <nombre>  fois 'I'
        attendu = 'V' + 'I' * (nombre - 5)
        self.assertEqual(attendu, result)

    def test_nine(self):
        # ETANT DONNE le chiffre 9
        nombre = 9

        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(nombre)

        # ALORS on obtient 'IX'
        self.assertEqual('IX', result)

    @parameterized.parameterized.expand([[10], [11], [12], [13]])
    def test_ten_to_thirteen(self, nombre):
        # ETANT DONNE un chiffre entre 10 à 13
        # QUAND on le convertit en nombres romains
        result = ConvertisseurNombresRomains.convertir(nombre)

        # ALORS on obtient 'V' + <nombre>  fois 'I'
        attendu = 'X' + 'I' * (nombre - 10)
        self.assertEqual(attendu, result)

if __name__ == '__main__':
    unittest.main()
