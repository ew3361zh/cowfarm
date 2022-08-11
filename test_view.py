import unittest 
from unittest import TestCase
from unittest.mock import MagicMock, patch

import builtins
import importlib

from view.view_util import input_positive_float
from view import view
import view_model
from model.pen_model import Pen

class TestView(TestCase):

    @patch('view.view_util.input_positive_float')
    @patch('builtins.input')
    def test_add_one_pen(self, mock_input_1, mock_positive_float_1, mock_input_2, mock_positive_float_2, mock_positive_float_3):
        mock_input_1.return_value = 'Holstein'
        mock_positive_float_1.return_value = 10
        mock_input_2.return_value = 'corn'
        mock_positive_float_2.return_value = 8
        mock_positive_float_3.return_value = 3

        importlib.reload(view)

        mock_view_model = MagicMock()
        mock_view_model.insert = MagicMock()

        test_view = view.View(mock_view_model)

        pen = Pen('Holstein', 10, corn, 8, 3)

        test_view.get_new_pen_data()

        mock_view_model.insert.assert_called_with(pen)