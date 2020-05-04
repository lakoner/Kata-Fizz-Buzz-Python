import unittest

from Fizzbuzz import Fizzbuzz

class FizzbuzzTest(unittest.TestCase):
    def test_fizz_calculador(self):
        fizzbuzz = Fizzbuzz()
        resultado = fizzbuzz.calculador(3)
        self.assertEqual('Fizz', resultado)

    def test_buzz_calculador(self):
        fizzbuzz = Fizzbuzz()
        resultado = fizzbuzz.calculador(5)
        self.assertEqual('Buzz', resultado)

    def test_fizzbuzz_calculador(self):
        fizzbuzz = Fizzbuzz()
        resultado = fizzbuzz.calculador(15)
        self.assertEqual('fizzbuzz', resultado)

    def test_not_fizzbuzz_calculador(self):
        fizzbuzz = Fizzbuzz()
        resultado = fizzbuzz.calculador(7)
        self.assertEqual(7, resultado)


