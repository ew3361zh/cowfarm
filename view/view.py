from model.pen_model import Pen
from view.view_util import header, input_positive_float
from exceptions.farm_error import FarmError


class View:

    def __init__(self, view_model):
        self.view_model = view_model

    def get_new_pens(self):

        header('Welcome to the RuFas-beta model, John!\nAdd information about a new pen')
        
        while True:
            pen = self.get_new_pen_data()
            if not pen:
                break
    
    def get_new_pen_data(self):

        print('*** For this pen: ***\n')
        breed = input('Enter the name of the breed of cow or press "enter" to quit: ')
        if not breed:
            return
        
        number_of_cows = input_positive_float(f'How many total {breed} does the pen hold? ')
        feed_type = input('What type of feed are you using? ')
        amount_of_feed_per_cow = input_positive_float('How many pounds of feed does one cow eat per day? ')
        feed_cost_per_pound = input_positive_float('How much (in dollars) does 1 pound of this feed cost? ')
        q1_milk_yield = input_positive_float('How much milk (in gallons) does the pen produce in Q1 (Jan-Mar)? ')
        q2_milk_yield = input_positive_float('How much milk (in gallons) does the pen produce in Q2 (Apr-Jun)? ')
        q3_milk_yield = input_positive_float('How much milk (in gallons) does the pen produce in Q3 (Jul-Sep)? ')
        q4_milk_yield = input_positive_float('How much milk (in gallons) does the pen produce in Q4 (Oct-Dec)? ')
        print()
        pen = Pen(breed, number_of_cows, feed_type, amount_of_feed_per_cow, feed_cost_per_pound, q1_milk_yield, q2_milk_yield, q3_milk_yield, q4_milk_yield)

        try:
            self.view_model.insert(pen)
            return pen
        except FarmError as e:
            print(str(e))

# import pandas
# import matplotlib.pyplot as plt

    # def run_time_series(self):

        

    
