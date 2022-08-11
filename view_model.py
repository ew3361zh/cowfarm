# model class to communicate between view and db

class ViewModel:

    def __init__(self, db):
        self.db = db

    def insert(self, pen):
        self.db.insert(pen)

    def get_all(self):
        return self.db.get_all()