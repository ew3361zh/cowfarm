import sqlite3

from .config import db_path
from exceptions.farm_error import FarmError
from model.pen_model import Pen
from view.view_util import input_positive_float

db = db_path

class SQLFarmDB():

    def __init__(self):
        with sqlite3.connect(db) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS pens (
                breed TEXT NOT NULL,
                number_of_cows INTEGER NOT NULL,
                feed_type TEXT,
                amount_of_feed_per_cow INTEGER NOT NULL,
                milk_yield INTEGER NOT NULL)"""
                )
        
        conn.close()
    
    def insert(self, pen):
        if pen is None:
            raise FarmError('No pen data available to save into database')

        else:
            with sqlite3.connect(db) as conn:
                conn.execute('INSERT INTO pens VALUES(?, ?, ?, ?, ?)',
                            (pen.breed,
                            pen.number_of_cows,
                            pen.feed_type,
                            pen.amount_of_feed_per_cow,
                            pen.milk_yield))
            conn.close()

    def get_all_pens(self):
        conn = sqlite3.connect(db)
        farm_cursor = conn.execute('SELECT * FROM pens')
        pens = [ Pen(*row) for row in farm_cursor.fetchall() ]
        conn.close()
        return pens