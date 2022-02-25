import unittest
from KataTDD.conjunto import Conjunto

class TestConjunto(unittest.TestCase):

    def test_conjunto_vacio(self):
        conjunto = Conjunto([5])
        #self.assertIsNone(conjunto.dar_promedio(),5)
        self.assertEqual(conjunto.dar_promedio(),5)