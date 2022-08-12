"""
John has a cattle farm which consists of a few pens. Each pen houses some cows. 
The cows in each pen are of the same breed. Each breed of cow eats only one type of feed, 
yields a certain amount of milk, and generates a certain level of greenhouse gases.

John has asked you to help him simulate his farm so he can foresee the consequences of his 
decisions. Develop a code based on OOP to simulate this cattle farm, and run a few scenarios 
to showcase how it works. Some example features of this simulation are: 

Pen allocation: What breed is allocated to this pen? How many cows are there?

Milk yield calculation: How much milk should we expect from each pen? Can you 
make a time series?

Greenhouse gas emissions: Overall, how much greenhouse gases does this scenario generate?

Estimates from online searches: 
1 dairy cow produces avg of 7.5 gallons milk/day 
https://www.ciwf.com/farmed-animals/cows/dairy-cows/#:~:text=Milk%20production%20per%20cow%20has,gallon%20of%20milk%20per%20day
1 liter of milk produces 1.39 kg of CO2 equivalents to the atmosphere
https://blogs.nicholas.duke.edu/citizenscientist/how-green-is-your-milk/
1 liter = 0.264172 gallons
7.5 gallons of milk produces ~2.7539931 kg of CO2 per day

Cost estimation: Based on the type and amount of the consumed feeds, how much does 
it cost John to implement this scenario in his farm?
"""

from view import *

from db.farm_database import SQLFarmDB

from view.view import View
from view_model import ViewModel


def main():

    farm_db = SQLFarmDB()

    farm_view_model = ViewModel(farm_db)

    farm_view = View(farm_view_model)

    farm_view.get_new_pens()

    

    print('\nWe hope this information was helpful to you!\n'
    'Feedback is encouraged as we continue to refine our model.\n' 
    'Please email rufas_dev_team@cornell.edu with your comments.\n' 
    'Thank you for using the RuFas-beta program!\n')


if __name__ == '__main__':
    main()