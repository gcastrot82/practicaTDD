import unittest
from KataTDD.conjunto import Conjunto

class TestConjunto(unittest.TestCase):

    def test_conjunto_vacio(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.dar_promedio())
        #self.assertEqual(conjunto.dar_promedio(),5)

    def test_conjunto_un_elemento(self):
        conjunto = Conjunto([5])
        #self.assertIsNone(conjunto.dar_promedio(),5)
        self.assertEqual(conjunto.dar_promedio(),5)

    def test_conjunto_dos_elementos(self):
        conjunto = Conjunto([5,7])
        self.assertEqual(conjunto.dar_promedio(),6)