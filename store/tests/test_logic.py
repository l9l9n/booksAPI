from unittest import TestCase

from store.tests.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(6, 13, '+')
        self.assertEquals(19, result)

    def test_minus(self):
        result = operations(6, 13, '-')
        self.assertEquals(-7, result)

    def test_multiple(self):
        result = operations(6, 13, '*')
        self.assertEquals(78, result)