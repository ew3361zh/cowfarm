import sqlite3
import unittest
from unittest import TestCase

from db import farm_database

from model.pen_model import Pen

from exceptions.farm_error import FarmError

class TestPenDB(TestCase):

    test_db = 'test_farm_pens.db'

    def setUp(self):
        farm_database.db = self.test_db


        with sqlite3.connect(self.test_db) as conn:
            conn.execute('DROP TABLE IF EXISTS pens')
        conn.close()

        with sqlite3.connect(self.test_db) as conn:
            conn.execute("""CREATE TABLE pens (
                breed TEXT NOT NULL,
                number_of_cows INTEGER NOT NULL,
                feed_type TEXT,
                amount_of_feed_per_cow INTEGER NOT NULL,
                milk_yield INTEGER NOT NULL)"""
                )
        conn.close()

        self.db = farm_database.SQLFarmDB()
    
    def test_add_new_pen(self):
        p1 = Pen('Holstein', 10, 'corn', 8, 3)
        self.db.insert(p1)
        expected = ('Holstein', 10, 'corn', 8, 3)
        row = 0
        self.compare_db_to_expected(expected, row)

        p2 = Pen('Simmental', 5, 'grain', 6, 2)
        self.db.insert(p2)
        expected = ('Simmental', 5, 'grain', 6, 2)
        row = 1 
        self.compare_db_to_expected(expected, row)

    
    def compare_db_to_expected(self, expected, row):
        conn = sqlite3.connect(self.test_db)
        all_data = conn.execute('SELECT * FROM pens').fetchall()[row]

        self.assertEqual(len(expected), len(all_data))
        self.assertEqual(all_data[0], expected[0])
        
        conn.close()