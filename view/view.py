from model.pen_model import Pen
from view.view_util import header, input_positive_float, calculate_annual_cost, calculate_annual_ghg
from exceptions.farm_error import FarmError

from datetime import datetime

# for time-series graphing
import matplotlib.pyplot as plt

"""User interface functions only. Database queries are passed to the ViewModel"""

class View:

    def __init__(self, view_model):
        self.view_model = view_model


    def get_new_pens(self):
        """welcome message and calling to get new pen input data from user"""
        header('Welcome to the Dairy Farm GHG model, John!\nAdd information about a new pen')
        
        while True:
            pen = self.get_new_pen_data()
            if not pen:
                break
    

    def get_new_pen_data(self):
        """Collect user data on pens, build pen objects, and call on the ViewModel to store pen objects to the database"""
        print('*** For this pen: ***\n')
        breed = input('Enter the name of the breed of cow or press "enter" to stop entering pen data and see comparison results: ')
        if not breed: #  user indicates they don't want to add more new pens by pressing enter key
            print()
            return
        
        number_of_cows = input_positive_float(f'How many total {breed} does the pen hold? ')
        feed_type = input('What type of feed are you using? ')
        amount_of_feed_per_cow = input_positive_float('How many pounds of feed does one cow eat per day? ')
        feed_cost_per_pound = input_positive_float('How much (in dollars) does 1 pound of this feed cost? ')
        q1_milk_yield = input_positive_float('How much milk (in gallons) does the pen produce in Q1 (Jan-Mar)? ')
        q2_milk_yield = input_positive_float('How much milk (in gallons) does the pen produce in Q2 (Apr-Jun)? ')
        q3_milk_yield = input_positive_float('How much milk (in gallons) does the pen produce in Q3 (Jul-Sep)? ')
        q4_milk_yield = input_positive_float('How much milk (in gallons) does the pen produce in Q4 (Oct-Dec)? ')
        print('Thank you, that\'s all the info we need for this pen - on to the next pen!')
        print()
        pen = Pen(breed, number_of_cows, feed_type, amount_of_feed_per_cow, feed_cost_per_pound, q1_milk_yield, q2_milk_yield, q3_milk_yield, q4_milk_yield)

        try:
            self.view_model.insert(pen)
            return pen
        except FarmError as e:
            print(str(e))


    def run_time_series(self):
        """time series to graph quarterly milk yields of all the different pens for which user entered data"""
        try:
            pens = self.view_model.get_all_pens()
            # matplotlib takes datetime objects so converting quarterly start dates to datetime objects for graphing
            quarters = [datetime(2022, 1, 1), datetime(2022, 4, 1), datetime(2022, 7, 1), datetime(2022, 10, 1)]  
            pen_count = 1
            for row in pens:
                milk_yields = [row.q1_milk_yield, row.q2_milk_yield, row.q3_milk_yield, row.q4_milk_yield]
                plt.rcParams['figure.figsize'] = [8.5, 5.5]  # set standard size of graph when it first opens
                line, = plt.plot_date(quarters, milk_yields, '-', marker='o')
                line.set_label(f'pen #{pen_count}: {row.breed}')  # for labeling different pen-lines in graph
                plt.ylabel('Milk Yield (In Gallons)')
                plt.legend(loc='best')  # 'best' option tries to automatically pick the legend location least likely to cover up plotted graph data
                pen_count += 1
            plt.title(f'Quarterly Milk Yield comparison')
            plt.show()
        except FarmError as e:
            print(str(e))
    

    def calculate_cost_and_ghg(self):
        """final calculation comparison of cost and ghg generation for each pen"""
        try:
            pens = self.view_model.get_all_pens()
            pen_count = 1
            for row in pens:
                annual_cost = calculate_annual_cost(row.number_of_cows, row.amount_of_feed_per_cow, row.feed_cost_per_pound)
                print(f'Pen #{pen_count} will yield {row.q1_milk_yield + row.q2_milk_yield + row.q3_milk_yield + row.q4_milk_yield} gallons of milk '+
                f'at a cost of ${annual_cost:.0f}')
                annual_ghg = calculate_annual_ghg(row.q1_milk_yield, row.q2_milk_yield, row.q3_milk_yield, row.q4_milk_yield)
                print(f'while generating {round(annual_ghg, 2)} kg of CO2 each year\n')
                pen_count += 1

        except FarmError as e:
            print(str(e))
        

    