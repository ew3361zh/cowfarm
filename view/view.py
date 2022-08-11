from model.pen_model import Pen
from view_util import header, input_positive_float
from exceptions.farm_error import FarmError


class View:

    def __init__(self, view_model):
        self.view_model = view_model

    def get_new_pens(self):

        header('Add information about a new pen')

        while True:
            pen = self.get_new_pen_data()
            if not pen:
                break
    
    def get_new_pen_data(self):

        print('For this pen:\n')
        breed = input('Enter the name of the breed of cow or press "enter" to quit: ')
        if not breed:
            return
        
        number_of_cows = input_positive_float(f'How many total {breed}s does it hold? ')
        feed_type = input('What type of feed are you using? ')
        amount_of_feed_per_cow = input_positive_float('How much feed does one cow eat per day? ')
        milk_yield = input_positive_float('How much milk on average does one cow produce per day? ')

        pen = Pen(breed, number_of_cows, feed_type, amount_of_feed_per_cow, milk_yield)

        try:
            self.view_model.add(pen)
            return pen
        except FarmError as e:
            print(str(e))



    
