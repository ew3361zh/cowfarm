import unittest
from unittest import TestCase
from model.pen_model import Pen


class TestPenModel(TestCase):

    def test_string(self):
        pen = Pen('Holstein', 10, 'corn', 35, 8, 100, 200, 300, 500)
        self.assertIn('Holstein', str(pen))
        self.assertIn('corn', str(pen))
        self.assertIn('10', str(pen))

